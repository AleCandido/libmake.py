class Prerequisite:
    def __init__(self, prerequisite):
        self.prerequisite = prerequisite


class PrerequisiteList:
    def __init__(self, prerequisites):
        self.prerequisites = []
        for prerequisite in prerequisites:
            self.prerequisites.append(Prerequisite(prerequisite))
