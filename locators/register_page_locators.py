from selenium.webdriver.common.by import By


class RegisterLocators:
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
