import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait

def test_create_ad_unauthorized_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    assert wait.until(EC.visibility_of_element_located(POPUP_WINDOW_LOGIN)), "Окно предупреждения об авторизации не появилось"

def test_create_ad_authorized_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(LOGIN_REG_BUTTON)).click()
    wait.until(EC.presence_of_element_located(EMAIL_FIELD)).send_keys(*LOGIN_TEST_USER)
    driver.find_element(*PASSWORD_FIELD).send_keys(*PASSWORD_TEST_USER)
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    time.sleep(5) 

    wait.until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()  

    wait.until(EC.url_contains("create-lisiting"))


    wait.until(EC.presence_of_element_located(NAME_AD_FIELD)).send_keys("Тестовое название")


    dropduwn_button_category = wait.until(EC.element_to_be_clickable(CATEGORY_AD_DROPDOWN))
    dropduwn_button_category.click()

    books_option = wait.until(EC.element_to_be_clickable(BOOKS_CATEGORY))
    books_option.click()


    dropduwn_button_city = wait.until(EC.element_to_be_clickable(CITY_AD_DROPDOWN))
    dropduwn_button_city.click()

    city_option = wait.until(EC.element_to_be_clickable(NOVOSYB_CITY))
    city_option.click()

    radio_button_state = wait.until(EC.presence_of_element_located(RADIO_BUTTON_AD))
    driver.execute_script("arguments[0].click();", radio_button_state)

    wait.until(EC.presence_of_element_located(NOTE_AD_FIELD)).send_keys("Тестовое описание")

    wait.until(EC.presence_of_element_located(COST_AD_FIELD)).send_keys("112")

    wait.until(EC.element_to_be_clickable(TO_PUBLISH_BUTTON)).click()

    search_element = wait.until(EC.presence_of_element_located(FOR_SEARCH_CREATED_AD))
    assert search_element is not None, "Объявление с названием 'Тестовое название' не найден"
    time.sleep(5)