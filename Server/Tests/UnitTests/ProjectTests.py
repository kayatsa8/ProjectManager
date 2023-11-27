import sys
sys.path.append("Server")

import unittest
from typing import List

from BusinessLayer.projects.Project import Project


name: str = "project1"
description: str = "description1"
languages: List[str] = ["Java", "Python", "C++"]
tools: List[str] = ["React.js", "MongoDB", "SQLite"]


class ProjectTests(unittest.TestCase):

    def setUp(self):
        self.project: Project = Project(name, description, languages, tools)

    def testTemp(self):
        self.assertTrue(True, "This supposed to pass")

        # right now Project just hold data, no real logic behind it


if __name__ == "__main__":
    unittest.main()
