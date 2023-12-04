from typing import List
from BusinessLayer.users.User import User


class ServiceUser:

    def __init__(self, user: User) -> None:
        self.username: str = user.getUsername()
        self.projects: List[str] = user.getAllProjectNames()

    def toDict(self) -> dict:
        return {
            "username": self.username,
            "projects": self.projects
        }