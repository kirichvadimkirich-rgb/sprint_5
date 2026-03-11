from tests import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdCreationUnauthorized:
    # Тест: Создание объявления неавторизованным пользователем
    def test_unauthorized_ad_creation_shows_auth_modal(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.POST_AND_AD_BUTTON)).click()
       
        # Ожидание появления  модального окна с заголовком
        modal_title = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.MODAL_TITLE))

        # Проверка соответсвия заголовка ожидаемому тексту
        assert modal_title.text.strip() == "Чтобы разместить объявление, авторизуйтесь"