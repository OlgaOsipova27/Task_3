import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_page import BasePage
from locators.main_page_locators import MainLocators
from locators.login_page_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть страницу логина')
    def open_login_page(self):
        self.click_element(MainLocators.LOGIN_ACCOUNT_BUTTON)
        self.wait_for_element(MainLocators.LOGIN_HEADER)

    @allure.step('Заполнить и отправить форму логина')
    def submit_login(self, email, password):
        self.fill_input(LoginLocators.EMAIL_INPUT, email)
        self.fill_input(LoginLocators.PASSWORD_INPUT, password)

        old_url = self.driver.current_url
        self.click_element(LoginLocators.LOGIN_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_changes(old_url))

    @allure.step('Авторизоваться пользователем с главной страницы')
    def login(self, email, password):
        self.open_login_page()
        self.submit_login(email, password)
