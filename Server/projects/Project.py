from typing import List
from datetime import date

class Project:

    def __init__(self, name: str, description: str, languages: List[str], tools: List[str]) -> None:
        self.__name: str = name
        self.__description: str = description
        self.__languages: List[str] = languages
        self.__tools: List[str] = tools
        self.__completed: bool = False
        self.__completionDate: date = date.max

    def getName(self) -> str:
        return self.__name
    
    def getDescription(self) -> str:
        return self.__description
    
    def getLanguages(self) -> List[str]:
        return self.__languages
    
    def getTools(self) -> List[str]:
        return self.__tools
    
    def isCompleted(self) -> bool:
        return self.__completed
    
    def getCompletionDate(self) -> date:
        return self.__completionDate
    
    