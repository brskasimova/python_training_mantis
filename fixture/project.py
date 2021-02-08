from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath(
                    "//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
                name = element.find_element_by_css_selector("td:nth-child(1)").text
                id_not_fetched = (element.find_element_by_xpath(
                    "//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/a").get_attribute(
                    "href"))
                id = id_not_fetched.replace(
                    "http://localhost/mantisbt-2.24.4/manage_proj_edit_page.php?project_id=", "")
                description = element.find_element_by_css_selector("td:nth-child(5)").text
                self.project_cache.append(Project(name=name, description=description, id=id))
        return list(self.project_cache)

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        self.return_to_project_page()
        self.project_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.get(self.app.base_url+'manage_proj_edit_page.php?project_id='+str(id))

    def open_project_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Управление").click()
            wd.find_element_by_link_text("Управление проектами").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Продолжить").click()