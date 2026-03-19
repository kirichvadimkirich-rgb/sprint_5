import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import string
from tests import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"
EXISTING_USER_EMAIL = "vadim55@testtov.com"
EXISTING_USER_PASSWORD = "Qwertytest987"

@pytest.fixture
def driver():
    #Фикстура для открытия и закрытия драйвера Chrome.
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")  
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def generate_random_email():
    chars = string.ascii_letters + string.digits
    local_part = ''.join(random.choices(chars, k=7))
    domain =  ''.join(random.choices(string.ascii_lowercase, k=7))
    tId = ''.join(random.choices(string.ascii_lowercase, k=3)) 
    return f"{local_part}@{domain}.{tId}"

@pytest.fixture
def generate_random_password():
    chars = string.ascii_letters + string.digits
    len = random.randint(5, 15)
    return ''.join(random.choices(chars, k=len))

@pytest.fixture
def get_credentials_email_password(driver, generate_random_email, generate_random_password):
        
    # Нажать кнопку  'Вход и регистрация'
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        
    # Нажать кнопку  'Нет аккаунта'
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()
        
    # Генерируем случайные данные
    email = generate_random_email      
    password = generate_random_password 

    # Заполнить поля регистрационной формы
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REPEAT_PASSWORD_INPUT).send_keys(password)

    # Нажать кнопку 'Создать аккаунт')
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.CREATE_AN_ACCOUNT_BUTTON)).click()

    # Нажать кнопку 'Выйти' из аккаунта главной страницы
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.EXIT_BUTTON)).click()

    # Возвращаем словарь с данными созданного пользователя
    return {"email": email, "password": password}