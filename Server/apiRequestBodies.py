from typing import List, TypedDict

class registerLoginBody(TypedDict):
    username: str
    password: str


class logOutBody(TypedDict):
    username: str


class changeUsernameBody(TypedDict):
    oldUsername: str
    newUsername: str
    password: str


class changePasswordBody(TypedDict):
    username: str
    oldPassword: str
    newPassword: str


class deleteUserBody(TypedDict):
    username: str
    password: str


class getProjectBody(TypedDict):
    username: str
    projectName: str


class addProjectBody(TypedDict):
    username: str
    projectName: str
    description: str
    languages: List[str]
    tools: List[str]


