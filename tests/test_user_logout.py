from tests import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestUserLogout:
   
    # Тест: Выход из системы под авторизованным пользователем
    def test_user_logout(self, driver):
        # Нажать кнопку  'Вход и регистрация'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
      
        # Заполнить поля существующими данными
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
     
        # Нажать кнопку  "Войти")
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_BUTTON)).click()
       
        # Нажать кнопку 'Выйти' из аккаунта главной страницы
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.EXIT_BUTTON)).click()

        # Ожидание успешного выхода (отсутствие аватара пользователя и имени пользователя)
        WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(locators.USER_AVATAR))
        WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(locators.USER_NAME))

        # Проверка отображения кнопки 'Вход и регистрация'
        login_and_registration_btn = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.LOGIN_AND_REGISTRATION_BUTTON))
        assert login_and_registration_btn.is_displayed()