from typing import List
from BusinessLayer.Facade import Facade
from BusinessLayer.projects.Project import Project
from BusinessLayer.users.User import User
from ServiceLayer.Objects.ServiceProject import ServiceProject
from ServiceLayer.Objects.ServiceUser import ServiceUser
from ServiceLayer.Response import Response


class Service:

    def __init__(self) -> None:
        self.__facade = Facade()

    def register(self, username: str, password: str) -> Response[bool]:
        try:
            self.__facade.register(username, password)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def logIn(self, username: str, password: str) -> Response[bool]:
        try:
            self.__facade.logIn(username, password)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def logOut(self, username: str) -> Response[bool]:
        try:
            self.__facade.logOut(username)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def changeUsername(self, oldUsername: str, newUsername:str, password: str) -> Response[bool]:
        try:
            self.__facade.changeUsername(oldUsername, newUsername, password)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def changePassword(self, username: str, oldPassword: str, newPassword: str) -> Response[bool]:
        try:
            self.__facade.changePassword(username, oldPassword, newPassword)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def getUser(self, username: str) -> Response[ServiceUser]:
        try:
            user: User = self.__facade.getUser(username)
            serviceUser: ServiceUser = ServiceUser(user)
            return Response.makeValueResponse(serviceUser)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def deleteUser(self, username: str, password: str) -> Response[bool]:
        try:
            self.__facade.deleteUser(username, password)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def getProject(self, username: str, projectName: str) -> Response[ServiceProject]:
        try:
            project: Project = self.__facade.getProject(username, projectName)
            serviceProject: ServiceProject = ServiceProject(project)
            return Response.makeValueResponse(serviceProject)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def addProject(self, username: str, projectName: str, description: str, languages: List[str], tools: List[str]) -> Response[bool]:
        try:
            self.__facade.addProject(username, projectName, description, languages, tools)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def deleteProject(self, username: str, projectName: str) -> Response[bool]:
        try:
            self.__facade.deleteProject(username, projectName)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def changeProjectName(self, username: str, projectName: str, newProjectName: str) -> Response[bool]:
        try:
            self.__facade.changeProjectName(username, projectName, newProjectName)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
        
    def changeProjectDescription(self, username: str, projectName: str, description: str) -> Response[bool]:
        try:
            self.__facade.changeProjectDescription(username, projectName, description)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))

    def changeProjectLanguages(self, username: str, projectName: str, languages: List[str]) -> Response[bool]:
        try:
            self.__facade.changeProjectLanguages(username, projectName, languages)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
    
    def changeProjectTools(self, username: str, projectName: str, tools: List[str]) -> Response[bool]:
        try:
            self.__facade.changeProjectTools(username, projectName, tools)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
    
    def markProjectCompleteIncomplete(self, username: str, projectName: str) -> Response[bool]:
        try:
            self.__facade.markProjectCompleteIncomplete(username, projectName)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))
    
    
