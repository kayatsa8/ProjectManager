import sys
sys.path.append("Server")

import unittest

from ServiceLayer.Service import Service
from ServiceLayer.Response import Response



username1: str = "username1"
password1: str = "password1"
username2: str = "username2"
password2: str = "password2"


class Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.service: Service = Service()

    def registerUsers(self) -> None:
        self.service.register(username1, password1)
        self.service.register(username2, password2)

    def registerAndLogIn(self) -> None:
        self.registerUsers()

        self.service.logIn(username1, password1)
        self.service.logIn(username2, password2)

    def testRegister_success(self):
        response: Response[bool] = self.service.register(username1, password1)
        self.assertFalse(response.isError(), "user1 did not register")

        response = self.service.register(username2, password2)
        self.assertFalse(response.isError(), "user2 did not register")

    def testRegister_fail(self):
        self.service.register(username1, password1)

        # register twice
        response: Response[bool] = self.service.register(username1, password1)
        self.assertTrue(response.isError(), "user1 registered twice")

        # register empty username
        self.service.register("", password2)
        self.assertTrue(response.isError(), "Empty username registered")

        # register short password
        self.service.register(username2, "12")
        self.assertTrue(response.isError(), "Short password registered")

    def testLogIn_success(self):
        self.registerUsers()

        response: Response[bool] = self.service.logIn(username1, password1)
        self.assertFalse(response.isError(), "user1 didn't log in")

        response = self.service.logIn(username2, password2)
        self.assertFalse(response.isError(), "user2 didn't log in")

    def testLogIn_fail(self):
        self.registerUsers()

        # log in to not existing users
        response: Response[bool] = self.service.logIn("dfgvsd", password1)
        self.assertTrue(response.isError(), "A user that does not exist logged in")

        # log in with bad password
        response = self.service.logIn(username1, "dfbdfv")
        self.assertTrue(response.isError(), "user1 logged in with bad password")

        # log in twice
        self.service.logIn(username1, password1)
        response = self.service.logIn(username1, password1)
        self.assertTrue(response.isError(), "user1 logged in twice")
    
    def testLogOut_success(self):
        self.registerAndLogIn()

        response: Response[bool] = self.service.logOut(username2)
        self.assertFalse(response.isError(), "user2 didn't log out")

        response = self.service.logOut(username1)
        self.assertFalse(response.isError(), "user1 didn't log out")

    def testLogOut_fail(self):
        self.registerUsers()

        # unregistered user
        response: Response[bool] = self.service.logOut("sdfd")
        self.assertTrue(response.isError(), "An unregistered user logged out")

        # user not logged in
        response = self.service.logOut(username2)
        self.assertTrue(response.isError(), "user2 not logged in but logged out")

        






if __name__ == "__main__":
    unittest.main()

