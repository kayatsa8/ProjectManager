from typing import Dict, List

from BusinessLayer.projects.Project import Project
from BusinessLayer.users.User import User

class Facade:
    
    def __init__(self) -> None:
        self.__users: Dict[str, User] = dict()  # (username, User)
        self.__passwordLength: int = 4

    ### Users

    def register(self, username: str, password: str) -> None:
        if len(username) < 1:
            raise Exception("Empty username")

        if username in self.__users:
            raise Exception("A user with the given username is already exist!")
        
        if not self.__isValidPassword(password):
            raise Exception("The password should be at least " + str(self.__passwordLength) + " characters")
        
        user: User = User(username, password)

        self.__users[username] = user      

    def __isValidPassword(self, password: str) -> bool:
        
        # 4 is arbitrary
        if len(password) < self.__passwordLength:
            return False
        
        return True

    def logIn(self, username: str, password: str) -> None:
        if username not in self.__users:
            raise Exception("No such user")
        
        self.__users[username].logIn(password)
        
    def logOut(self, username: str) -> None:
        if username not in self.__users:
            raise Exception("No such user")
        
        self.__users[username].logOut()

    def changeUsername(self, oldUsername: str, newUsername: str, password: str) -> None:
        if oldUsername not in self.__users:
            raise Exception("No such user")
        
        if newUsername in self.__users:
            raise Exception("The username is already taken")
        
        user: User = self.__users[oldUsername]

        user.changeUsername(newUsername, password)

        self.__users[newUsername] = self.__users.pop(oldUsername)

    def changePassword(self, username: str, oldPassword: str, newPassword: str) -> None:
        if username not in self.__users:
            raise Exception("No such user")
        
        if not self.__isValidPassword(newPassword):
            raise Exception("The new password is invalid")
        
        user: User = self.__users[username]
        user.changePassword(oldPassword, newPassword)

    def getUser(self, username: str) -> User:
        if username not in self.__users:
            raise Exception("no such user")
        
        return self.__users[username]
    
    def deleteUser(self, username: str, password: str) -> None:
        if username not in self.__users:
            raise Exception("No such user")
        
        if not self.__users[username].canDelete(password):
            raise Exception("The user cannot be deleted right now, please try again to enter your password")
        
        self.__users.pop(username, None)

    
    ### Projects

    def __userSearchException(self, username: str) -> None:
         if username not in self.__users:
            raise Exception("No such user")
         
    def __userLoggedInException(self, user: User) -> None:
        if not user.isLoggedIn():
            raise Exception("The user is not logged in")

    def getProject(self, username: str, projectName: str) -> Project:
        self.__userSearchException(username)
        
        user: User = self.__users[username]

        self.__userLoggedInException(user)
        
        return user.getProject(projectName)
    
    def addProject(self, username: str, projectName: str, description: str, languages: List[str], tools: List[str]) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.addProject(projectName, description, languages, tools)

    def deleteProject(self, username: str, projectName: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.deleteProject(projectName)

    def changeProjectName(self, username: str, projectName: str, newProjectName: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectName(projectName, newProjectName)
    
    def changeProjectDescription(self, username: str, projectName: str, description: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectDescription

    def changeProjectLanguages(self, username: str, projectName: str, languages: List[str]) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectLanguages(projectName, languages)

    def changeProjectTools(self, username: str, projectName: str, tools: List[str]) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectTools(projectName, tools)

    def markProjectCompleteIncomplete(self, username: str, projectName: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.markProjectCompleteIncomplete(projectName)

