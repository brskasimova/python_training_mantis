from model.project import Project
import random


def test_delete_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(name='testname', description='testdesc'))
    old_projects = app.soap.get_projects_list_for_user(app.admin_username, app.admin_password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.project_id)
    new_projects = app.soap.get_projects_list_for_user(app.admin_username, app.admin_password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)

