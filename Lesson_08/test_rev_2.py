import requests
from pages.authorization_page import Authorization
from pages.list_page import ClientsList

base_url = "https://ru.yougile.com"

auth = Authorization("https://ru.yougile.com")
client = ClientsList("https://ru.yougile.com")

# Позитивный тест. Создание проекта


def test_create_projects_positive():
    user_id = client.get_client_id()
    headers = auth.get_company_id()
    project = {
        "title": "Новый проект",
        "users": {user_id: "worker"}
    }
    resp = requests.post(
        base_url + "/api-v2/projects", json=project, headers=headers)
    assert resp.status_code == 201

# негативный тест. Создание проекта с некорректным ключом авторизации


def test_create_projects_negative():
    user_id = client.get_client_id()
    headers = auth.get_company_id()
    headers["Authorization"] = "123"

    project = {
        "title": "Новый проект",
        "users": {user_id: "worker"}
    }
    resp = requests.post(
        base_url + "/api-v2/projects", json=project, headers=headers)
    assert resp.status_code == 401

# Позитивный тест. Изменить проект


def test_change_project_positive():
    user_id = client.get_client_id()
    headers = auth.get_company_id()
    project_id = client.get_list_projects()

    project = {
        "title": "Измененный проект",
        "users": {user_id: "worker"}
    }
    resp = requests.put(
        base_url + "/api-v2/projects/" + project_id, json=project, headers=headers)
    assert resp.status_code == 200

# Негативный тест. Изменить проект без указания id проекта


def test_change_project_negative():
    user_id = client.get_client_id()
    headers = auth.get_company_id()

    project = {
        "title": "Измененный проект",
        "users": {user_id: "worker"}
    }
    resp = requests.put(
        base_url + "/api-v2/projects/", json=project, headers=headers)
    assert resp.status_code == 404

# Позитивный тест. Получение проекта по id.


def test_get_project_positive():
    headers = auth.get_company_id()
    project_id = client.get_list_projects()

    resp = requests.get(
        base_url + "/api-v2/projects/" + project_id, headers=headers)
    assert resp.status_code == 200

# Негативный тест. Запрос проекта с несуществующим id


def test_get_project_negative():
    headers = auth.get_company_id()
    project_id = client.get_list_projects()

    resp = requests.get(
        base_url + "/api-v2/projects/" + project_id + "1", headers=headers)
    assert resp.status_code == 404
