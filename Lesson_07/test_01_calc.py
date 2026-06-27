import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


new_delay_time = "45"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    page = CalcPage(driver)

    page.delay_input(new_delay_time)
    page.calc_sum()

    result = page.calc_result()

    assert result == "15"
