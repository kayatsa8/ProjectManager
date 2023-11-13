from typing import Dict
from users.User import User

class Facade:
    
    def __init__(self) -> None:
        self.__users: Dict[str, User] = dict()  # (username, User)
        self.__passwordLength: int = 4

    def register(self, username: str, password: str) -> None:
        if username is None or username in self.__users:
            raise Exception("A user with the given username is already exist!")
        
        if not self.__isValidPassword(password):
            raise Exception("The password should be at least " + str(self.__passwordLength) + " characters")
        
        user: User = User(username, password)

        self.__users[username] = user      

    def __isValidPassword(self, password: str) -> bool:
        if password is None:
            return False
        
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
            raise Exception("zno such user")
        
        return self.__users[username]
    
    def deleteUser(self, username: str, password: str) -> None:
        if username not in self.__users:
            raise Exception("No such user")
        
        if not self.__users[username].canDelete(password):
            raise Exception("The user cannot be deleted right now, please try again to enter your password")
        
        self.__users.pop(username, None)