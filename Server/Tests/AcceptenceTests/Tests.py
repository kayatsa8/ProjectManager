import sys
sys.path.append("Server")

import unittest
from typing import List

from ServiceLayer.Service import Service
from ServiceLayer.Response import Response


# users
username1: str = "username1"
password1: str = "password1"
username2: str = "username2"
password2: str = "password2"

# projects
projectName1: str = "project1"
description1: str = "description1"
languages1: List[str] = ["Java"]
tools1: List[str] = ["Eclipse"]
projectName2: str = "project2"
description2: str = "description2"
languages2: List[str] = ["Python"]
tools2: List[str] = ["Colab"]



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

    def testChangeUsername_success(self):
        self.registerAndLogIn()

        response: Response[bool] = self.service.changeUsername(username1, "username1.1", password1)

        self.assertFalse(response.isError(), "user1's username did not change")

    def testChangeUsername_fail(self):

        # user does not exist
        response: Response[bool] = self.service.changeUsername(username1, "sdvdsv", password1)
        self.assertTrue(response.isError(), "A user that does not exist changed his username")

        self.registerAndLogIn()

        # change username to an existing one
        response = self.service.changeUsername(username1, username2, password1)
        self.assertTrue(response.isError(), "user1 changed his username to user2's username")

        # user is not logged in
        self.service.logOut(username1)
        response = self.service.changeUsername(username1, "username1.1", password1)
        self.assertTrue(response.isError(), "user1 changed username while not logged in")

        # bad password
        response = self.service.changeUsername(username2, "username2.2", password1)
        self.assertTrue(response.isError(), "user2 changed username with bad password")

    def testChangePassword_success(self):
        self.registerAndLogIn()

        response: Response[bool] = self.service.changePassword(username2, password2, "password2.2")

        self.assertFalse(response.isError(), "user2 couldn't change password")

    def testChangePassword_fail(self):

        # user does not exist
        response: Response[bool] = self.service.changePassword(username2, password2, password1)
        self.assertTrue(response.isError(), "A user that does not exist changed his password")

        # user not logged in
        self.registerUsers()
        response = self.service.changePassword(username2, password2, password1)
        self.assertTrue(response.isError(), "user2 change password while logged out")

        self.service.logIn(username2, password2)

        # invalid old password
        response = self.service.changePassword(username2, password1, password1)
        self.assertTrue(response.isError(), "user2 change password with bad old password")

        # invalid new password
        response = self.service.changePassword(username2, password2, "148")
        self.assertTrue(response.isError(), "user2 change password to invalid one")

    def testDeleteUser_success(self):
        self.registerAndLogIn()

        response: Response[bool] = self.service.deleteUser(username2, password2)

        self.assertFalse(response.isError(), "user2 is not deleted")

    def testDeleteUser_fail(self):

        response: Response[bool]

        # user not registered
        response = self.service.deleteUser(username2, password2)
        self.assertTrue(response.isError(), "user2 was deleted but is not registered")
        
        self.registerUsers()

        # user not logged in
        response = self.service.deleteUser(username2, password2)
        self.assertTrue(response.isError(), "user2 was deleted while logged out")

        self.service.logIn(username2, password2)

        # bad password
        response = self.service.deleteUser(username2, password1)
        self.assertTrue(response.isError(), "user2 was deleted with bad password")

    def testAddProject_success(self):
        response: Response[bool]
        self.registerAndLogIn()

        # add fisrt project
        response = self.service.addProject(username1, projectName1, description1, languages1, tools1)
        self.assertFalse(response.isError(), "user1 cannot add first project")

        # add second project
        response = self.service.addProject(username1, projectName2, description2, languages2, tools2)
        self.assertFalse(response.isError(), "user1 cannot add second project")

        # add same first project to second user
        response = self.service.addProject(username2, projectName1, description1 ,languages1, tools1)
        self.assertFalse(response.isError(), "user2, cannot add first project")

    def testAddProject_fail(self):
        response: Response[bool]

        # user not registered
        response = self.service.addProject(username1, projectName1, description1, languages1, tools1)
        self.assertTrue(response.isError(), "user1 added project without being registered")

        self.registerUsers()

        # user not logged in
        response = self.service.addProject(username1, projectName1, description1, languages1, tools1)
        self.assertTrue(response.isError(), "user1 added project without being logged in")

        self.service.logIn(username1, password1)

        # project name taken
        self.service.addProject(username1, projectName1, description1, languages1, tools1)
        response = self.service.addProject(username1, projectName1, description2, languages2, tools2)
        self.assertTrue(response.isError(), "user1 added 2 projects with the same name")

        



if __name__ == "__main__":
    unittest.main()

