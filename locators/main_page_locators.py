from selenium.webdriver.common.by import By


class MainLocators:
    LOGO_SVG = (By.CSS_SELECTOR, "svg[viewBox='0 0 290 50']")

    LOGIN_ACCOUNT_BUTTON = (By.XPATH,"//button[normalize-space()='Войти в аккаунт']")

    PERSONAL_ACCOUNT_LINK = (By.XPATH,"//a[@href='/account' and .//p[normalize-space()='Личный Кабинет']]")
    CONSTRUCTOR_LINK = (By.XPATH,"//p[normalize-space()='Конструктор']")
    FEED_LINK = (By.XPATH,"//p[normalize-space()='Лента Заказов']")
    LOGIN_HEADER = (By.XPATH,"//h2[normalize-space()='Вход']")
    REGISTER_LINK = (By.XPATH,"//a[@href='/register']")
    FORGOT_PASSWORD_LINK = (By.XPATH,"//a[@href='/forgot-password' and normalize-space()='Восстановить пароль']")

    BUN_CRATER_CARD = (By.XPATH,"//a[.//img[@alt='Краторная булка N-200i'] or .//img[@alt='Флюоресцентная булка R2-D3']]")
    BUN_CRATER_COUNTER = (By.XPATH,"//a[.//img[@alt='Краторная булка N-200i'] or .//img[@alt='Флюоресцентная булка R2-D3']]//*[contains(@class,'counter_counter__num')]")
    INGREDIENT_DETAILS_HEADER = (By.XPATH,"//h2[normalize-space()='Детали ингредиента']")
    INGREDIENT_DETAILS_MODAL = (By.XPATH,"//div[contains(@class,'Modal_modal__container')][.//h2[normalize-space()='Детали ингредиента']]")
    MODAL_CLOSE_BUTTON = (By.XPATH,"//button[contains(@class,'Modal_modal__close')]")

    CONSTRUCTOR_BUN_TOP_DROP_AREA = (By.XPATH,"//div[contains(@class,'constructor-element_pos_top')]")
    CONSTRUCTOR_DROP_AREA = (By.XPATH,"//ul[contains(@class,'BurgerConstructor_basket__list')]")
    CONSTRUCTOR_BUN_TOP_TEXT = (By.XPATH,"//span[contains(@class,'constructor-element__text') and contains(text(),'Флюоресцентная булка R2-D3 (верх)')]")
    CONSTRUCTOR_BUN_BOTTOM_TEXT = (By.XPATH,"//span[contains(@class,'constructor-element__text') and contains(text(),'Флюоресцентная булка R2-D3 (низ)')]")

    ORDER_BUTTON = (By.XPATH,"//button[normalize-space()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH,"//section[contains(@class,'Modal_modal_opened')]")
    ORDER_NUMBER = (By.XPATH,"//h2[contains(@class,'Modal_modal__title_shadow')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BUN_COUNTER = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")


class PasswordRecoveryLocators:
    PASSWORD_RECOVERY_HEADER = (By.XPATH,"//h2[text()='Восстановление пароля']")
    INPUT_NAME = (By.CSS_SELECTOR, "input[name='name']")
    RECOVERY_BUTTON = (By.XPATH,"//button[text()='Восстановить']")
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    PASSWORD_SHOW_HIDE_BUTTON = (By.XPATH,"//input[@type='password']/following-sibling::div[contains(@class,'input__icon')]")
    PASSWORD_INPUT_CONTAINER = (By.XPATH,"//label[normalize-space()='Пароль']/parent::div")


