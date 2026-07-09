import pytest
import allure
from selenium import webdriver
from pages.calc_page import CalcPage

new_delay_time = "45"


@pytest.fixture
def driver():
    with allure.step("Открытие браузера на тестируемой странице"):
        driver = webdriver.Chrome()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.title("Проверка функциональности калькулятора в браузере Chrome")
@allure.description("Тестирования установки времени задержки вывода результата и функции сложения")
@allure.feature("Delay; Sum")
@allure.severity("blocker")
def test_calc(driver):
    page = CalcPage(driver)

    page.delay_input(new_delay_time)
    page.calc_sum()

    with allure.step("Проверка итоговой суммы"):
        result = page.calc_result()
        assert result == "15"
