from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_projects = app.project.get_projects_list()
    project = Project(name=random_string("test", 10), description=random_string("test", 10))
    app.project.create(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_projects_list(),
                                                                 key=Project.id_or_max)
