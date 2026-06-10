from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
