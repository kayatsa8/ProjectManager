from typing import Dict, List
from BusinessLayer.projects.Project import Project


class User:

    def __init__(self, username: str, password: str) -> None:
        self.__username: str = username
        self.__password: str = password
        self.__loggedIn: bool = False
        self.__projects: Dict[str, Project] = dict()  # (projectName, Project)
        

    def logIn(self, password: str) -> None:
        if self.__loggedIn:
            raise Exception("The user is already logged in!")
        
        if self.__password is not password:
            raise Exception("The given password is not correct!")
        
        self.__loggedIn = True

    def logOut(self) -> None:
        if not self.__loggedIn:
            raise Exception("The user is not logged in!")
        
        self.__loggedIn = False

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
    
    ### projects

    def __searchProjectException(self, projectName: str) -> None:
        if not projectName in self.__projects:
            raise Exception("The project does not exist")

    def getProject(self, projectName: str) -> Project:
        self.__searchProjectException(projectName)
        
        return self.__projects[projectName]
    
    def addProject(self, name: str, description: str, languages: List[str], tools: List[str]) -> None:
        if name in self.__projects:
            raise Exception("A project eith that name already exists")
        
        project: Project = Project(name, description, languages, tools)

        self.__projects[name] = project

    def deleteProject(self, projectName: str) -> None:
        self.__searchProjectException(projectName)
        
        self.__projects.pop(projectName, None)

    def changeProjectName(self, projectName: str, newProjectName: str) -> None:
        self.__searchProjectException(projectName)

        if newProjectName in self.__projects:
            raise Exception("A project with that name already exists")
        
        project: Project = self.__projects[projectName]
        project.changeName(newProjectName)

        self.__projects[newProjectName] = self.__projects.pop(projectName)

    def changeProjectDescription(self, projectName: str, description: str) -> None:
        self.__searchProjectException(projectName)

        self.__projects[projectName].changeDescription(description)

    def changeProjectLanguages(self, projectName: str, languages: List[str]) -> None:
        self.__searchProjectException(projectName)

        self.__projects[projectName].changeLanguages(languages)

    def changeProjectTools(self, projectName: str, tools: List[str]) -> None:
        self.__searchProjectException(projectName)

        self.__projects[projectName].changeTools(tools)

    def markProjectCompleteIncomplete(self, projectName: str) -> None:
        self.__searchProjectException(projectName)

        self.__projects[projectName].markCompleteIncomplete()

    def getAllProjectNames(self) -> List[str]:
        return list(self.__projects.keys())

    ### use only for DB
    
    def getPassword(self) -> str:
        return self.__password
    
    def getProjects(self) -> Dict[str, Project]:
        return self.__projects
    
    def setUsername(self, username: str) -> None:
        self.__username = username

    def setPassword(self, password: str) -> None:
        self.__password = password

    def setLoggedIn(self, loggedIn: bool) -> None:
        self.__loggedIn = loggedIn

    def setProjects(self, projects: Dict[str, Project]) -> None:
        self.__projects = projects