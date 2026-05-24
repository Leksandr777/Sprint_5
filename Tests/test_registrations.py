import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import generate_email
from selenium.webdriver.support.ui import WebDriverWait

class TestRegistration:

    def test_valid_registration(self,driver):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        email = generate_email()
        wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(email)
        driver.find_element(*PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys("qwerty123")

        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.url_contains("regiatration"))
        assert wait.until(EC.visibility_of_element_located(USER_AVATAR)), "Аватар пользователя не найден"

        user_name_element = driver.find_element(*USER_NAME)
        assert user_name_element.text == "User.", f"User. не найдено"

    def test_invalid_email_format(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys("bad_email_mail.ru")
        driver.find_element(*PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        assert  wait.until(EC.visibility_of_element_located(MYSTAKE_MESSAGE)), "Ошибка не отобразилась"

        mystakes_border = driver.find_elements(*MYSTAKE_BORDERS)
        assert  len(mystakes_border)>=3, "Не все поля ввода не подсвечены красным"

    def test_register_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click() 

        #регистрация тестового юзера первичная
        first_email = generate_email()
        wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(first_email)
        driver.find_element(*PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()  

        #регистрация тестового юзера повторная
        wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click() 
        wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(first_email)
        driver.find_element(*PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys("qwerty123")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        assert  wait.until(EC.visibility_of_element_located(MYSTAKE_MESSAGE)), "Ошибка не отобразилась"

        mystakes_border = driver.find_elements(*MYSTAKE_BORDERS)
        assert  len(mystakes_border)>=3, "Не все поля ввода не подсвечены красным"

