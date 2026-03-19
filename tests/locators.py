from selenium.webdriver.common.by import By

# ----------------------Главная страница неавторизированного пользователя--------------------------
LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
POST_AND_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")

# ----------------------Окно Войти--------------------------
NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
# ----------------------Окно Зарегистрироваться--------------------------
EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
EMAIL_FIELD = (By.XPATH, "//input[@name='email']/parent::div")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
PASSWORD_FIELD = (By.XPATH, "//input[@name='password']/parent::div")
REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@name='submitPassword']/parent::div")
CREATE_AN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
MESSAGE_ERROR = (By.XPATH, ".//span[text()='Ошибка']")

# ----------------------Главная страница после залогинивания--------------------------
USER_AVATAR = (By.CSS_SELECTOR, "svg.svgSmall")
USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
USER_AVATAR_BUTTON = (By.XPATH, "//button[@class='circleSmall']")

#--------------Модальное окно Разместить объявление неавторизированного пользователя---------------
MODAL_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

#-----------------------страница Новое объявление---------------------------------------
NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description'][placeholder='Описание товара']")
PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown')]")
CATEGORY_TECHNOLOGIES = (By.XPATH, "//span[text()='Технологии']")
CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown')]")
CITY_NOVOSIBIRSK = (By.XPATH, "//span[text()='Новосибирск']")
USED_RADIOBUTTON = (By.XPATH, "//input[@name='condition']/following-sibling::div[contains(@class, 'radioUnput_inputR')]")
PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

#-------------------------------страница профиль----------------------------------
CARD_LAST = (By.CSS_SELECTOR, "div.card:last-of-type")