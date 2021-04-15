from sys import maxsize


class Project:

    def __init__(self, project_id=None, name=None, description=None):
        self.project_id = project_id
        self.name = name
        self.description = description

    def __repr__(self):
        return "Project(id={}, name={}, description={})".format(self.project_id, self.name, self.description)

    def __eq__(self, other):
        return (self.project_id == other.project_id or self.project_id is None or other.project_id is None) and \
               self.name == other.name and self.description == other.description

    def id_or_max(self):
        if self.project_id:
            return int(self.project_id)
        else:
            return maxsize