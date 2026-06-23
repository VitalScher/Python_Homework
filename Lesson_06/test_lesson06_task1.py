from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()

    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = driver.find_element(By.CSS_SELECTOR, "div[id='start'] button")
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    message = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div[id='finish'] h4"), "Hello World!")
        )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("lesson_06/screenshots/lesson_06_task1_screen.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    message_element = driver.find_element(By.CSS_SELECTOR, "div[id='finish'] h4")
    assert message_element.text == "Hello World!", "Текст 'Hello World!' не отобразился."

    driver.quit()
