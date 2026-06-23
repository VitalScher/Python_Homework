from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()

    sleep(1)

    link = driver.find_element(By.LINK_TEXT, "HTML form")
    link.click()

    sleep(4)

    check_url = "https://httpbin.org/forms/post"
    assert driver.current_url == check_url
    
    driver.back()
    assert driver.current_url == "https://httpbin.org/"
    
    driver.quit()
