from typing import Dict
from User import User

class UserFacade:
    
    def __init__(self) -> None:
        self.__users: Dict[str, User] = dict()
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
        
