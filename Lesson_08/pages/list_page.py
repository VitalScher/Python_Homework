import requests
from pages.authorization_page import Authorization

auth = Authorization("https://ru.yougile.com")

# Получение списка сотрудников


class ClientsList:

    def __init__(self, base_url):
        self.url = base_url

    def get_client_id(self):
        headers = auth.get_company_id()
        resp = requests.get(self.url + "/api-v2/users", headers=headers)
        assert resp.json()["paging"]["count"] > 0
        user_id = resp.json()["content"][0]["id"]
        return user_id

    def get_list_projects(self):
        headers = auth.get_company_id()
        resp = requests.get(self.url + "/api-v2/projects", headers=headers)
        assert resp.json()["paging"]["count"] > 0
        project_id = resp.json()["content"][0]["id"]
        return project_id
