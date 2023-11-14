from typing import List
from Server.BusinessLayer.users.User import User


class ServiceUser:

    def __init__(self, user: User) -> None:
        self.username: str = user.getUsername()
        self.projects: List[str] = user.getAllProjectNames()