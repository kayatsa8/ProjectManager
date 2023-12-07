from typing import List, TypedDict

class registerLoginHelper(TypedDict):
    username: str
    password: str



class addProjectHelper(TypedDict):
    username: str
    projectName: str
    description: str
    languages: List[str]
    tools: List[str]