from typing import Dict, List
from Server.projects.Project import Project


class User:

    def __init__(self, username: str, password: str) -> None:
        self.__username: str = username
        self.__password: str = password
        self.__loggedIn: bool = False
        self.__projects: Dict[str, Project] = dict()  # (projectName, Project)
        # TODO: (?) add id

    def logIn(self, password: str) -> None:
        if self.__loggedIn:
            raise Exception("The user is already logged in!")
        
        if self.__password is not password:
            raise Exception("The given password is not correct!")
        
        self.__loggedIn = True

    def logOut(self) -> None:
        if not self.__loggedIn:
            raise Exception("The user is not logged in!")
        
        self.__loggedIn = True

    def isLoggedIn(self) -> bool:
        return self.__loggedIn
    
    def changeUsername(self, newUsername: str, password: str) -> None:
        if not self.__loggedIn:
            raise Exception("The user is not logged-in")
        
        if password is not self.__password:
            raise Exception("The given password is not correct!")
        
        self.__username = newUsername

    def changePassword(self, oldPassword: str, newPassword: str) -> None:
        if not self.__loggedIn:
            raise Exception("The user is not logged-in")
        
        if oldPassword is not self.__password:
            raise Exception("The given password is not correct!")
        
        self.__password = newPassword

    def getUsername(self) -> str:
        return self.__username
    
    def canDelete(self, password: str) -> bool:
        if not self.__loggedIn:
            return False
        
        if password is not self.__password:
            return False
        
        return True
    
    def getProject(self, projectName: str) -> Project:
        if not projectName in self.__projects:
            raise Exception("The project does not exist")
        
        return self.__projects[projectName]
    
    def addProject(self, name: str, description: str, languages: List[str], tools: List[str]) -> None:
        if name in self.__projects:
            raise Exception("A project eith that name already exists")
        
        project: Project = Project(name, description, languages, tools)

        self.__projects[name] = project

    def deleteProject(self, projectName: str) -> None:
        if not projectName in self.__projects:
            raise Exception("No such project")
        
        self.__projects.pop(projectName, None)