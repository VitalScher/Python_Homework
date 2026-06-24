from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    input_first_name = driver.find_element(By.NAME, "first-name")
    input_first_name.send_keys("Иван")

    input_second_name = driver.find_element(By.NAME, "last-name")
    input_second_name.send_keys("Петров")

    input_address = driver.find_element(
        By.CSS_SELECTOR, "input[name='address']")
    input_address.send_keys("Ленина, 55-3")

    input_email = driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']")
    input_email.send_keys("test@skypro.com")

    input_phone_number = driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']")
    input_phone_number.send_keys("+7985899998787")

    input_city = driver.find_element(
        By.CSS_SELECTOR, "input[name='city']")
    input_city.send_keys("Москва")

    input_country = driver.find_element(
        By.CSS_SELECTOR, "input[name='country']")
    input_country.send_keys("Россия")

    input_job_position = driver.find_element(By.NAME, "job-position")
    input_job_position.send_keys("QA")

    input_company = driver.find_element(
        By.CSS_SELECTOR, "input[name='company']")
    input_company.send_keys("SkyPro")

    submit_btn = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    zip_code_alert = driver.find_element(
        By.XPATH, "//div[@id='zip-code']")
    assert zip_code_alert.get_attribute("class") == "alert py-2 alert-danger"

    first_name_alert = driver.find_element(
        By.XPATH, "//div[@id='first-name']")
    assert first_name_alert.get_attribute("class") == "alert py-2 alert-success"

    second_name_alert = driver.find_element(
        By.XPATH, "//div[@id='last-name']")
    assert second_name_alert.get_attribute("class") == "alert py-2 alert-success"

    address_alert = driver.find_element(
        By.XPATH, "//div[@id='address']")
    assert address_alert.get_attribute("class") == "alert py-2 alert-success"

    email_alert = driver.find_element(
        By.XPATH, "//div[@id='e-mail']")
    assert email_alert.get_attribute("class") == "alert py-2 alert-success"

    phone_number_alert = driver.find_element(
        By.XPATH, "//div[@id='phone']")
    assert phone_number_alert.get_attribute("class") == "alert py-2 alert-success"

    city_alert = driver.find_element(
        By.XPATH, "//div[@id='city']")
    assert city_alert.get_attribute("class") == "alert py-2 alert-success"

    country_alert = driver.find_element(
        By.XPATH, "//div[@id='country']")
    assert country_alert.get_attribute("class") == "alert py-2 alert-success"

    job_position_alert = driver.find_element(
        By.XPATH, "//div[@id='job-position']")
    assert job_position_alert.get_attribute("class") == "alert py-2 alert-success"

    company_alert = driver.find_element(
        By.XPATH, "//div[@id='company']")
    assert company_alert.get_attribute("class") == "alert py-2 alert-success"

    driver.quit()
