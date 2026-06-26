from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    delay_time = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_time.clear()
    delay_time.send_keys("45")

    seven_btn = driver.find_element(By.XPATH, "//span[normalize-space()='7']")
    seven_btn.click()

    plus_btn = driver.find_element(By.XPATH, "//span[normalize-space()='+']")
    plus_btn.click()

    eight_btn = driver.find_element(By.XPATH, "//span[normalize-space()='8']")
    eight_btn.click()

    equally_btn = driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-warning']")
    equally_btn.click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@class='screen']"), "15")
    )
    calc_sum = driver.find_element(By.XPATH, "//div[@class='screen']")
    assert calc_sum.text == "15"

    driver.quit()
