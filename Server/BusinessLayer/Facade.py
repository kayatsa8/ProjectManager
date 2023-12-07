from typing import Dict, List

from BusinessLayer.projects.Project import Project
from BusinessLayer.users.User import User
from PersistenceLayer.DataController import DataController

class Facade:
    
    def __init__(self, testMode: bool = False) -> None:
        self.__users: Dict[str, User] = dict()  # (username, User)
        self.__passwordLength: int = 4
        self.__dataController = DataController(testMode)

    
    ### Users

    def register(self, username: str, password: str) -> None:
        if len(username) < 1:
            raise Exception("Empty username")

        if username in self.__users:
            # TODO: BUGFIX: search in DB
            raise Exception("A user with the given username is already exist!")
        
        if not self.__isValidPassword(password):
            raise Exception("The password should be at least " + str(self.__passwordLength) + " characters")
        
        user: User = User(username, password)

        self.__users[username] = user

        self.__dataController.createUser(user)

    def __isValidPassword(self, password: str) -> bool:
        
        # 4 is arbitrary
        if len(password) < self.__passwordLength:
            return False
        
        return True

    def logIn(self, username: str, password: str) -> None:
        if username not in self.__users:
            try:
                user: User = self.__dataController.readUser(username)
                self.__users[username] = user
            except:
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

        self.__dataController.updateUser(oldUsername, user)

    def changePassword(self, username: str, oldPassword: str, newPassword: str) -> None:
        if username not in self.__users:
            raise Exception("No such user")
        
        if not self.__isValidPassword(newPassword):
            raise Exception("The new password is invalid")
        
        user: User = self.__users[username]
        user.changePassword(oldPassword, newPassword)

        self.__dataController.updateUser(username, user)

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

        self.__dataController.deleteUser(username)

    
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

        self.__dataController.updateUser(username, user)

    def deleteProject(self, username: str, projectName: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.deleteProject(projectName)

        self.__dataController.updateUser(username, user)

    def changeProjectName(self, username: str, projectName: str, newProjectName: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectName(projectName, newProjectName)

        self.__dataController.updateUser(username, user)
    
    def changeProjectDescription(self, username: str, projectName: str, description: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectDescription(projectName, description)

        self.__dataController.updateUser(username, user)

    def changeProjectLanguages(self, username: str, projectName: str, languages: List[str]) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectLanguages(projectName, languages)

        self.__dataController.updateUser(username, user)

    def changeProjectTools(self, username: str, projectName: str, tools: List[str]) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.changeProjectTools(projectName, tools)

        self.__dataController.updateUser(username, user)

    def markProjectCompleteIncomplete(self, username: str, projectName: str) -> None:
        self.__userSearchException(username)

        user: User = self.__users[username]

        self.__userLoggedInException(user)

        user.markProjectCompleteIncomplete(projectName)

        self.__dataController.updateUser(username, user)

    # for tests only; will have no effect in real run
    def emptyDB(self) -> None:
        self.__dataController.emptyDB()