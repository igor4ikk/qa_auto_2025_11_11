import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.basket
def test_add_item_to_basket():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.amazon.com/")

    search_product = driver.find_element(By.ID, "twotabsearchtextbox")
    search_product.send_keys("shoes")
    search_product.send_keys(Keys.ENTER)

    link = driver.find_element(By.XPATH, "//a[contains(@href, '/dp/B0DJVBW5SB')]")
    link.click()
    
    wait = WebDriverWait(driver, 8)

#    add_to_list = wait.until(EC.element_to_be_clickable((By.ID, "add-to-wishlist-button-submit")))
#    add_to_list.click()

    time.sleep(30)

    driver.close()