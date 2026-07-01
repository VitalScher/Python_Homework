import pytest
from selenium import webdriver
from pages.shop_forms_page import ShopFormsPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    page = ShopFormsPage(driver)

    page.authorization()
    page.shop()
    page.cart()
    page.input_personal_data()
    page.sum()

    result = page.sum()

    assert result == "Total: $58.29"
