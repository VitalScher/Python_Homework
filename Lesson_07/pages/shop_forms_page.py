from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopFormsPage:

    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    SL_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SL_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    SL_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.XPATH, "//button[@id='checkout']")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_SUM = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'login': "standard_user",
            'password': "secret_sauce",
            'first_name': "Иван",
            'last_name': "Петров",
            'zip_code': "100200"
        }

    def authorization(self):
        input_login = self.driver.find_element(*self.USER_NAME)
        input_login.send_keys(self.fields["login"])

        input_password = self.driver.find_element(*self.PASSWORD)
        input_password.send_keys(self.fields['password'])

        login_btn = self.driver.find_element(*self.LOGIN_BTN)
        login_btn.click()

    def shop(self):
        self.wait.until(EC.url_contains("/inventory"))

        sl_backpack = self.driver.find_element(*self.SL_BACKPACK)
        sl_backpack.click()

        sl_shirt = self.driver.find_element(*self.SL_SHIRT)
        sl_shirt.click()

        sl_onesie = self.driver.find_element(*self.SL_ONESIE)
        sl_onesie.click()

        shopping_cart = self.driver.find_element(*self.SHOPPING_CART)
        shopping_cart.click()

    def cart(self):
        self.wait.until(EC.url_contains("/cart"))

        checkout_btn = self.driver.find_element(*self.CHECKOUT_BTN)
        checkout_btn.click()

    def input_personal_data(self):
        self.wait.until(EC.url_contains("/checkout-step-one"))

        input_first_name = self.driver.find_element(*self.FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys(self.fields['first_name'])

        input_last_name = self.driver.find_element(*self.LAST_NAME)
        input_last_name.clear()
        input_last_name.send_keys(self.fields['last_name'])

        input_zip_code = self.driver.find_element(*self.ZIP_CODE)
        input_zip_code.clear()
        input_zip_code.send_keys(self.fields['zip_code'])

        continue_btn = self.driver.find_element(*self.CONTINUE_BTN)
        continue_btn.click()

    def sum(self):
        self.wait.until(EC.url_contains("/checkout-step-two"))

        total_sum = self.driver.find_element(*self.TOTAL_SUM)
        return total_sum.text
