import allure

from page_object.base_page import BasePage
from locators.main_page_locators import MainLocators


class RecovPassPage(BasePage):

    @allure.step('Открываем страницу логина')
    def open_login_page_login_button(self):
        self.click_element(MainLocators.LOGIN_ACCOUNT_BUTTON)
        self.wait_for_element(MainLocators.LOGIN_HEADER)
