from .target import Target
from .prerequisite import PrerequisiteList
from .recipe import Recipe


class Rule:
    def __init__(self, target, prerequisites, recipe):
        self.target = Target(target)
        self.prerequisites = PrerequisiteList(prerequisites)
        self.recipe = Recipe(recipe)

    def __contains__(self, target):
        return self.target.match(target)

    def __lt__(self, prerequisite):
        return prerequisite in self.prerequisites

    def run(self):
        # self.recipe(self.target, self.prerequisites)
        self.recipe()

    def get_target(self):
        return self.target

    def get_prerequisites(self):
        return self.prerequisites
