from tests import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import BASE_URL
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class TestUserRegistration:
    # Тест успешной регистрации нового пользователя
    def test_user_registration_successful(self, driver, generate_random_email, generate_random_password):
        # Нажать кнопку 'Вход и регистрация'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()

        # Нажать кнопку  "Нет аккаунта" для переключения на регистрацию
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()
        
        # Генерируем случайные данные
        email = generate_random_email     
        password = generate_random_password 

        # Заполнить поля регистрационной формы
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REPEAT_PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.CREATE_AN_ACCOUNT_BUTTON)).click()
       
        # Ожидание успешного входа (появление аватара пользователя)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.USER_AVATAR))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.USER_NAME))

        # Проверка url главной страницы
        assert driver.current_url == BASE_URL

        # Проверка отображения имени пользователя и сверка текста имени пользователя 
        user_name_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.USER_NAME))
        assert user_name_element.text.strip() == "User."
        

    # Тест регистрации пользователя с некорректным email (без @)
    def test_registration_with_invalid_email_should_fail(self, driver, generate_random_email):
        # Нажать кнопку  'Вход и регистрация'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()

        # Нажать кнопку  "Нет аккаунта"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

        # Ввод некорректного email (без @)
        invalid_email = generate_random_email.replace("@", "")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(invalid_email)

        # Нажать кнопку  "Cоздать аккаунт"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.CREATE_AN_ACCOUNT_BUTTON)).click()

        # Проверка появления сообщения об ошибке, сверка текста ошибки
        message_error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.MESSAGE_ERROR))
        assert  message_error.text == 'Ошибка', \
        f"Ожидалось сообщение с текстом 'Ошибка', получено сообщение {message_error.text}"

        # Проверка красной рамки у поля 'Email'
        email_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
        assert email_field.value_of_css_property('border-color') == 'rgb(255, 105, 114)'

        # Проверка красной рамки у поля 'Пароль'
        password_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
        assert password_field.value_of_css_property('border-color') == 'rgb(255, 105, 114)'

        # Проверка красной рамки у поля 'Повторите пароль'
        repeat_password_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.REPEAT_PASSWORD_FIELD))
        assert repeat_password_field.value_of_css_property('border-color') == 'rgb(255, 105, 114)'
       

    # Тест регистрации уже существующего пользователя
    def test_registration_with_existing_user_should_fail(self, driver, get_credentials_email_password):
        # Получаем данные созданного пользователя
        creds = get_credentials_email_password
        email = creds["email"] 
        password = creds["password"]

        # Нажать кнопку 'Вход и регистрация'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        
        # Нажать кнопку 'Нет аккаунта'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

         # Заполнить поля регистрационной формы существующими данными
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REPEAT_PASSWORD_INPUT).send_keys(password)

        # Нажать кнопку  'Создать аккаунт'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.CREATE_AN_ACCOUNT_BUTTON)).click()

        # Проверка появления сообщения об ошибке, сверка текста ошибки
        message_error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.MESSAGE_ERROR))
        assert  message_error.text == 'Ошибка', \
        f"Ожидалось сообщение с текстом 'Ошибка', получено сообщение {message_error.text}"

        # Проверка красной рамки у поля 'Email'
        email_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
        assert email_field.value_of_css_property('border-color') == 'rgb(255, 105, 114)'

        # Проверка красной рамки у поля 'Пароль'
        password_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
        assert password_field.value_of_css_property('border-color') == 'rgb(255, 105, 114)'

        # Проверка красной рамки у поля 'Повторите пароль'
        repeat_password_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.REPEAT_PASSWORD_FIELD))
        assert repeat_password_field.value_of_css_property('border-color') == 'rgb(255, 105, 114)'
    