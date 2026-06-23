from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")
    driver.maximize_window()

    driver.add_cookie({
        "name": "SESSION",
        "value": "ZjliOGFmYWMtYTU0Ni00YjBmLTlhYzEtZGMwNTIyMmUyNjhm",
        "domain": "gitflic.ru"
        })

    driver.refresh()

    driver.get("https://gitflic.ru/user/qa1")
    driver.save_screenshot("lesson_06/screenshots/lesson_06_task2_screen1.png")

    url_1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "NTFhN2RlODYtZTJiMC00ZjQ5LWIwNDItMDRkNWM3Yjk3ZThl",
        "domain": "gitflic.ru"
        })

    driver.refresh()

    driver.get("https://gitflic.ru/user/qa2")
    driver.save_screenshot("lesson_06/screenshots/lesson_06_task2_screen2.png")

    url_2 = driver.current_url

    assert url_1 != url_2

    driver.quit()
