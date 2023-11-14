from typing import List
from Server.BusinessLayer.projects.Project import Project
from datetime import date


class ServiceProject:

    def __init__(self, project: Project) -> None:
        self.name: str = project.getName()
        self.description: str = project.getDescription()
        self.languages: List[str] = project.getLanguages()
        self.tools: List[str] = project.getTools()
        self.completed: bool = project.isCompleted()
        self.completionDate: date = project.getCompletionDate()