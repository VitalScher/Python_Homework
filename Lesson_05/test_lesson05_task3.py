from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    
    links = driver.find_elements(By.TAG_NAME, "a")
    
    for i, link in enumerate(links):
        assert link.is_displayed()
        if i == 0:
            assert links[i].text == "1"
        else:
            AssertionError('Текст первой ссылки содержит "1"')
    
    assert len(links) == 9

    driver.quit