import allure

from page_object.base_page import BasePage
from locators.main_page_locators import MainLocators
from locators.register_page_locators import RegisterLocators
from locators.login_page_locators import LoginLocators


class RegisterPage(BasePage):

    @allure.step('Открыть страницу регистрации')
    def open_register_page(self):
        self.click_element(MainLocators.LOGIN_ACCOUNT_BUTTON)
        self.wait_for_element(MainLocators.LOGIN_HEADER)
        self.click_element(MainLocators.REGISTER_LINK)

    @allure.step('Зарегистрировать пользователя')
    def register(self, name, email, password):
        self.open_register_page()
        self.fill_input(RegisterLocators.NAME_INPUT, name)
        self.fill_input(RegisterLocators.EMAIL_INPUT, email)
        self.fill_input(RegisterLocators.PASSWORD_INPUT, password)
        self.click_element(RegisterLocators.REGISTER_BUTTON)
        self.wait_for_element(MainLocators.LOGIN_HEADER)
