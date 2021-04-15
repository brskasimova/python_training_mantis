from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_projects = app.soap.get_projects_list_for_user(app.admin_username, app.admin_password)
    project = Project(name=random_string("test", 10), description=random_string("test", 10))
    app.project.create(project)
    new_projects = app.soap.get_projects_list_for_user(app.admin_username, app.admin_password)
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
