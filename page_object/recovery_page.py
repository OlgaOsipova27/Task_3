import allure
from data.url import URL_FORGOT_PASS
from locators.main_page_locators import MainLocators
from locators.main_page_locators import PasswordRecoveryLocators as passloc
from page_object.base_page import BasePage
from data.user_data import TEST_EMAIL

class RecovPassPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Открытие страницы восстановления пароля")
    def open(self):
        self.driver.get(URL_FORGOT_PASS)
        self.wait_for_visible_element(passloc.PASSWORD_RECOVERY_HEADER)
    
    @allure.step("Переход на страницу восстановления пароля со страницы логина")
    def go_to_password_recovery(self):
        self.click_element(MainLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step("Проверка, что находимся на странице восстановления пароля")
    def is_recovery_page(self):
        return self.driver.current_url == URL_FORGOT_PASS
    
    @allure.step("Восстановление пароля по email")
    def recover_password(self):
    
        self.fill_input(passloc.INPUT_NAME, TEST_EMAIL)
        self.click_element(passloc.RECOVERY_BUTTON)
        self.wait_for_visible_element(passloc.NEW_PASSWORD_INPUT)
    
    @allure.step("Поле нового пароля отображается")
    def is_new_password_form_displayed(self):
        return self.find_element(passloc.NEW_PASSWORD_INPUT).is_displayed()
    
    @allure.step("Клик по кнопке показать/скрыть пароль")
    def toggle_password_visibility(self):
        self.click_element(passloc.PASSWORD_SHOW_HIDE_BUTTON)
    
    @allure.step("Проверка что поле пароля активно")
    def is_password_field_active(self):
        container_class = self.find_element(passloc.PASSWORD_INPUT_CONTAINER).get_attribute("class")
        return "input_status_active" in container_class

    @allure.step("Открыть старницу логина с главной страницы")
    def open_recovery_page(self):
        self.open_main_page()
        self.click_element(MainLocators.LOGIN_ACCOUNT_BUTTON)