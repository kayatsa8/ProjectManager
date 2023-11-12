class User:

    def __init__(self, username: str, password: str) -> None:
        self.username: str = username
        self.password: str = password
        self.loggedIn: bool = False
        # TODO: a list of projects
        # TODO: (?) add id

    def logIn(self, password: str) -> None:
        if self.loggedIn:
            raise Exception("The user is already logged in!")
        
        if self.password is not password:
            raise Exception("The given password is not correct!")
        
        self.loggedIn = True

    def logOut(self) -> None:
        if not self.loggedIn:
            raise Exception("The user is not logged in!")
        
        self.loggedIn = True

    def isLoggedIn(self) -> bool:
        return self.loggedIn