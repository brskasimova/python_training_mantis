from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.soap_url = app.base_url + "api/soap/mantisconnect.php?wsdl"

    def get_projects_list_for_user(self, user, password):
        client = Client(self.soap_url)
        try:
            soap_projects = client.service.mc_projects_get_user_accessible(user, password)
        except WebFault:
            return None
        projects = [Project(project_id=x.id, name=x.name, description=x.description) for x in soap_projects]
        return projects