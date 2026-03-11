from tests import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD, BASE_URL


class TestUserLogin:
    # Тест: успешный вход в систему под существующим пользователем
    def test_user_login_successful(self, driver):
        # Нажать кнопку 'Вход и регистрация'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
      
        # Заполнить поля существующими данными
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)

        # Нажать кнопку "Войти")
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_BUTTON)).click()

        # Ожидание успешного входа (появление аватара пользователя)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.USER_AVATAR))

        # Проверка url главной страницы
        assert driver.current_url == BASE_URL

        # Проверка отображения имени пользователя и сверка текста имени пользователя 
        user_name_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.USER_NAME))
        assert user_name_element.text.strip() == "User."
         