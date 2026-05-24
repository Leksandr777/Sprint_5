import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

def test_login_existing_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)

    wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()

    email_field = wait.until(EC.presence_of_element_located(EMAIL_FIELD))
    email_field.clear()
    email_field.send_keys(LOGIN_TEST_USER)

    password_field = driver.find_element(*PASSWORD_FIELD)
    password_field.clear()
    password_field.send_keys(PASSWORD_TEST_USER)

    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    wait.until(EC.url_contains("login"))

    assert wait.until(EC.visibility_of_element_located(USER_AVATAR)), "Аватар пользователя не найден"

    user_name_element = driver.find_element(*USER_NAME)
    assert user_name_element.text == "User.", f"User. не найдено"


def test_logout_existing_user(driver):
    #логин созданного пользователя
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
    wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(*LOGIN_TEST_USER)
    driver.find_element(*PASSWORD_FIELD).send_keys(*PASSWORD_TEST_USER)
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    wait.until(EC.url_contains("login"))

    wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

    assert  wait.until(EC.visibility_of_element_located(LOGIN_REG_BUTTON)), "Аватар пользователя все еще отображается"