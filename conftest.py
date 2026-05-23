import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def generate_email():

    text_mail = 'new_user'
    return f"{text_mail}{random.randint(1,10000)}@testmail.com"

