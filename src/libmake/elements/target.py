import fnmatch

from .prerequisite import PrerequisiteList
from ..utils.file import File


class Target:
    """Target.

    Note
    ----
    The main goal of this class is to provide an API to be used by MObject, and
    not to be used directly.

    So :meth:`__init__` will be replaced and not used, but it is here as an
    interface to specify the requirements to be fullfilled to be able to use the
    defined API, and on the other side what is available for API development.

    """

    def __init__(self, pattern, prerequisites=None):
        self.pattern = pattern

        prerequisites = [] if prerequisites is None else prerequisites
        self.prerequisites = PrerequisiteList(prerequisites)

    def __repr__(self):
        return self.pattern

    def match(self, target):
        return fnmatch.fnmatch(target, self.pattern)

    def is_up_to_date(self):
        try:
            File(self.pattern)
        except ValueError:
            # if the target it's not a path it's not up-to-date by definition
            return False
