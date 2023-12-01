from typing import Optional, Dict, List, Set
from pymongo import MongoClient
from datetime import date

from BusinessLayer.users.User import User
from BusinessLayer.projects.Project import Project


class DataController:

    def __init__(self) -> None:
        client = MongoClient("mongodb://localhost:27017")
        db = client.ProjectManagerDB
        self.userCollection = db.Users
        
    # CRUD

    def createUser(self, user: User) -> None:
        userDict: dict = self.userToDict(user)

        self.userCollection.insert_one(userDict)

    def readUser(self, username: str) -> User:
        userDict: Optional[dict] = self.userCollection.find_one({"username": username})

        if userDict is None:
            raise Exception("can't read the user")
        
        user: User = self.dictToUser(userDict)

        return user

    def updateUser(self, originalUsername: str, user: User) -> None:
        dbUser: User = self.readUser(originalUsername)

        if not dbUser.getUsername() == user.getUsername():
            self.__updateUsername(dbUser.getUsername(), user.getUsername())

        if not dbUser.getPassword() == user.getPassword():
            self.__updatePassword(user.getUsername(), user.getPassword())

        self.__updateProjects(user)

    def deleteUser(self, username: str) -> None:
        self.userCollection.delete_one({"username": username})

    
    # helpers

    def userToDict(self, user: User) -> dict:
        return {
            "username": user.getUsername(),
            "password": user.getPassword(),
            "projects": self.userProjectsToDict(user)
        }

    def dictToUser(self, userDict: dict) -> User:
        user: User = User("temp", "temp")

        user.setUsername(userDict["username"])
        user.setPassword(userDict["password"])
        user.setLoggedIn(False)
        user.setProjects(self.projectDictsToProjects(userDict))

        return user
    
    def userProjectsToDict(self, user: User) -> Dict[str, dict]:
        projects: Dict[str, Project] = user.getProjects()

        return {projectName: self.projectToDict(projects[projectName]) for projectName in projects}

    def projectToDict(self, project: Project) -> dict:
        return {
            "name": project.getName(),
            "description": project.getDescription(),
            "languages": project.getLanguages(),
            "tools": project.getTools(), 
            "completed": project.isCompleted(),
            "completionDate": self.dateToString(project.getCompletionDate())
        }
    
    def dateToString(self, d: date) -> str:
        return str(d.day) + "/" + str(d.month) + "/" + str(d.year)

    def projectDictsToProjects(self, userDict: dict) -> Dict[str, Project]:
        projects: dict = userDict["projects"]

        return {projectName: self.projectDictToProject(projects[projectName]) for projectName in projects}

    def projectDictToProject(self, projectDict: dict) -> Project:
        project: Project = Project("temp", "temp", [], [])

        project.setName(projectDict["name"])
        project.setDescription(projectDict["description"])
        project.setLanguages(projectDict["languages"])
        project.setTools(projectDict["tools"])
        project.setCompleted(projectDict["completed"])
        project.setCompletionDate(self.dateStringToDate(projectDict["completionDate"]))

        return project

    def dateStringToDate(self, dateString: str) -> date:
        dateList: List[int] = [int(string) for string in dateString.split("/")]

        return date(dateList[2], dateList[1], dateList[0])
    
    def __updateUsername(self, originalUsername: str, newUsername: str) -> None:
        self.userCollection.update_one({"username": originalUsername}, {"$set": {"username": newUsername}})

    def __updatePassword(self, username: str, password: str) -> None:
        self.userCollection.update_one({"username": username}, {"$set": {"password": password}})

    def __updateProjects(self, user: User) -> None:
        projectDict: Dict[str, dict] = self.userProjectsToDict(user)

        self.userCollection.update_one({"username": user.getUsername()}, {"$set": {"projects": projectDict}})
