import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait



def test_login_existing_user(driver):
    # первичное создание юзера 1 раз
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    try:
        wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(*LOGIN_TEST_USER)
        driver.find_element(*PASSWORD_FIELD).send_keys(*PASSWORD_TEST_USER)
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys(PASSWORD_TEST_USER)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        
        try:
            wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
            print("Пользователь успешно создан, выполняем выход")
            wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
       
        except TimeoutException:
            wait.until(EC.visibility_of_element_located(MYSTAKE_MESSAGE))
            print("Пользователь уже существует, пропускаем регистрацию")
            wait.until(EC.element_to_be_clickable(EXIST_ACCOUNT_BUTTON)).click()
            driver.get(MAIN_URL)
            wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()

    except Exception as e:
        print("Пропускаем регистрацию и переходим к логину существующего пользователя")
        # Возвращаемся на страницу логина
        driver.get(MAIN_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
            
    #логин созданного пользователя
    wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(*LOGIN_TEST_USER)
    driver.find_element(*PASSWORD_FIELD).send_keys(*PASSWORD_TEST_USER)
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