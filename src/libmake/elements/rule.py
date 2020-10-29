from .target import Target
from .prerequisite import PrerequisiteList
from .recipe import Recipe


class Rule:
    def __init__(self, target, prerequisites, recipe):
        self.target = Target(target)
        self.prerequisites = PrerequisiteList(prerequisites)
        self.recipe = Recipe(recipe)
