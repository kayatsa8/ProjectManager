import sys
sys.path.append("Server")

import unittest

from BusinessLayer.users.User import User

username: str = "username"
password: str = "password"


class UserTests(unittest.TestCase):

    def setUp(self):
        self.user: User = User(username, password)

    def testLogIn_success(self):
        self.user.logIn(password)

        self.assertTrue(self.user.isLoggedIn(), "The user is not logged in")

    def testLogIn_fail(self):
        with self.assertRaises(Exception):
            self.user.logIn("dfsd")

        self.assertFalse(self.user.isLoggedIn(), "The user is logged in")

    def testLogOut_success(self):
        self.user.logIn(password)
        self.user.logOut()

        self.assertFalse(self.user.isLoggedIn(), "The user is logged in")

    def testLogOut_fail(self):
        with self.assertRaises(Exception):
            self.user.logOut()

    def testChangeUsername_success(self):
        self.user.logIn(password)
        self.user.changeUsername("username1", password)

        self.assertEqual(self.user.getUsername(), "username1", "The username was not changed")        

    def testChangeUsername_fail(self):
        self.user.logIn(password)

        with self.assertRaises(Exception):
            self.user.changeUsername("username1", "sfsd")

        
        self.user.logOut()

        with self.assertRaises(Exception):
            self.user.changeUsername("username2", password)

    def testChangePassword_success(self):
        self.user.logIn(password)

        self.user.changePassword(password, "1234")
        self.user.logOut()
        self.user.logIn("1234")

        self.assertTrue(self.user.isLoggedIn(), "The password was not changed")

    def testChangePassword_fail(self):
        with self.assertRaises(Exception):
            self.user.changePassword(password, "1234")

        self.user.logIn(password)

        with self.assertRaises(Exception):
            self.user.changePassword("dfdvds", "1234")


if __name__ == "__main__":
    unittest.main()
