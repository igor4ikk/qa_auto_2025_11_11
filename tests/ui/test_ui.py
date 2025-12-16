import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():

    # створюєм обєкт для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://github.com/login")

    log_element = driver.find_element(By.ID, "login_field")
    log_element.send_keys("kiyunihor@notcorrect.com")

    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("error password")

    btn_elem = driver.find_element(By. NAME, "commit")
    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()