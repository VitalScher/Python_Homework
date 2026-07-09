import allure
import pytest
from selenium import webdriver
from pages.shop_forms_page import ShopFormsPage


@pytest.fixture
def driver():
    with allure.step("Открытие браузера на тестируемой странице"):
        driver = webdriver.Firefox()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.title("Проверка функциональности интернет-магазина в браузере Firefox")
@allure.description("Тестирование функций авторизации, добавления товаров в корзину, заполнения формы данных почтового адреса и итоговой страницы заказа")
@allure.feature("Authorization; Shop; Cart; Personal Data; Sum")
@allure.severity("blocker")
def test_shop(driver):
    page = ShopFormsPage(driver)

    page.authorization()
    page.shop()
    page.cart()
    page.input_personal_data()
    page.sum()

    with allure.step("Проверка итоговой суммы"):
        result = page.sum()
        assert result == "Total: $58.29"
