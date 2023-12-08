from typing import List
from BusinessLayer.projects.Project import Project
from datetime import date


class ServiceProject:

    def __init__(self, project: Project) -> None:
        self.name: str = project.getName()
        self.description: str = project.getDescription()
        self.languages: List[str] = project.getLanguages()
        self.tools: List[str] = project.getTools()
        self.completed: bool = project.isCompleted()
        self.completionDate: date = project.getCompletionDate()

    def toDict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "languages": self.languages,
            "tools": self.tools,
            "completed": self.completed,
            "completionDate": self.parseDate(d=self.completionDate)
        }
    
    def parseDate(self ,d: date) -> str:
        return str(d.day) + "/" + str(d.month) + "/" + str(d.year)