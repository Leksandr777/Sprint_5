from selenium.webdriver.common.by import By

MAIN_URL = "https://qa-desk.education-services.ru/"

LOGIN_REG_BUTTON = (By.XPATH, '//button[contains(text(), "Вход и регистрация")]')
LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
CREATE_AD_BUTTON = (By.XPATH, '//button[contains(text(), "Разместить объявление")]')

NO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Нет аккаунта")]')
EXIST_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Уже есть аккаунт")]')


EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']")
PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']")
CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Повторите пароль']")
CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Создать аккаунт")]')


USER_AVATAR = (By.CLASS_NAME, "svgSmall")
USER_NAME = (By.CLASS_NAME, "profileText")
LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выйти")]')

MYSTAKE_MESSAGE = ((By.CSS_SELECTOR, "span.input_span__yWPqB"))
MYSTAKE_BORDERS = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9')

LOGIN_TEST_USER = "test1@mail.ru"
PASSWORD_TEST_USER = "qwerty123"

POPUP_WINDOW_LOGIN = (By.CLASS_NAME, "popUp_titleRow__M7tGg")

NAME_AD_FIELD = (By.XPATH, "//input[@placeholder='Название']")
CATEGORY_AD_DROPDOWN = (By.XPATH,'//div[@class="dropDownMenu_dropMenu__sBxhz"]//input[@name="category"]/following::button[@class="dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP"][1]')
BOOKS_CATEGORY = (By.XPATH,'//div[@class="dropDownMenu_optionsMobile__LmXZM"]//button//span[contains(text(), "Книги")]')

CITY_AD_DROPDOWN = (By.XPATH,'//div[@class="dropDownMenu_dropMenu__sBxhz"]//input[@name="city"]/following::button[@class="dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP"][1]')
NOVOSYB_CITY = (By.XPATH,'//div[@class="dropDownMenu_optionsMobile__LmXZM"]//button//span[contains(text(), "Новосибирск")]')

NOTE_AD_FIELD = (By.XPATH, "//textarea[@placeholder='Описание товара']")
COST_AD_FIELD = (By.XPATH, "//input[@placeholder='Стоимость']")

RADIO_BUTTON_AD = (By.XPATH,'//input[@name="condition" and @value="Б/У"]')

TO_PUBLISH_BUTTON = (By.XPATH, '//button[contains(text(), "Опубликовать")]')

FOR_SEARCH_CREATED_AD = (By.XPATH,'//div[@class="card" and .//h2[contains(text(), "Тестовое название")]]')