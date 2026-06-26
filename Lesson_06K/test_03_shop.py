from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    input_login = driver.find_element(By.ID, "user-name")
    input_login.send_keys("standard_user")

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    sl_backpack = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack")
    sl_backpack.click()

    sl_shirt = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    sl_shirt.click()

    sl_onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    sl_onesie.click()

    shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/cart"))

    checkout_btn = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_btn.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one"))

    input_first_name = driver.find_element(By.ID, "first-name")
    input_first_name.clear()
    input_first_name.send_keys("Иван")

    input_last_name = driver.find_element(By.ID, "last-name")
    input_last_name.clear()
    input_last_name.send_keys("Петров")

    input_zip_code = driver.find_element(By.ID, "postal-code")
    input_zip_code.clear()
    input_zip_code.send_keys("100200")

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-two"))

    total_sum = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    sum = total_sum.text

    driver.quit()

    assert sum == "Total: $58.29"
