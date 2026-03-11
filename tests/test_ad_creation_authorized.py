from tests import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time
class TestAdCreationAuthorized:
    # Тест: Создание объявления авторизованным пользователем
    def test_ad_creation_authorized_successful(self, driver, get_credentials_email_password):
        # Получаем данные созданного пользователя
        creds = get_credentials_email_password
        email = creds["email"] 
        password = creds["password"]
       
        # Нажать кнопку 'Вход и регистрация'
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        
        # Заполнить поля существующими данными
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(email )
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password )
        time.sleep(15)
        # Нажать кнопку"Войти")
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LOGIN_BUTTON)).click()
      
        # Нажать кнопку 'Разместить объявление'
        button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locators.POST_AND_AD_BUTTON))
        ActionChains(driver).move_to_element(button).click().perform()
       
        # Заполнить поля объявления
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.NAME_INPUT)).send_keys("Продам IPHONE 18 PRO")
        driver.find_element(*locators.DESCRIPTION_INPUT).send_keys("1 месяц использования, состояние идеальное")
        driver.find_element(*locators.PRICE_INPUT).send_keys(70000)

        # Выбрать категорию 'Технологии' из выпадающего списка
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.CATEGORY_DROPDOWN)).click()
        driver.find_element(*locators.CATEGORY_TECHNOLOGIES).click()

        # Выбрать города 'Новосибирск' из выпадающего списка
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.CITY_DROPDOWN)).click()
        driver.find_element(*locators.CITY_NOVOSIBIRSK).click()

        # Выставить радиокнопкиу - б\у
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.USED_RADIOBUTTON)).click()

        # Нажать кнопку "Опубликовать"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.PUBLISH_BUTTON)).click()

        # Нажать на аватар (ActionChains для надёжности)
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locators.USER_AVATAR_BUTTON))
        ActionChains(driver).move_to_element(element).click().perform()
        
        # Проверка, что созданная карточка содержит название, город и цену
        card = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.CARD_LAST))
        card_text = card.text
        assert "Продам IPHONE 18 PRO" in card_text
        assert "Новосибирск" in card_text
        assert "70 000 ₽" in card_text
