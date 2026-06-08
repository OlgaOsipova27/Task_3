import pytest
import allure

from page_object.base_page import BasePage
from page_object.recovery_page import RecovPassPage
from page_object.login_page import LoginPage
from page_object.main_page import MainPage


class TestRecoveryPassword:

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.base_page = BasePage(driver)
        self.recovery_page = RecovPassPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)

    @allure.title('Переход по кнопке "Восстановить пароль" открывает страницу восстановления')
    def test_click_on_button_recovery_password_open_recovery_page(self):
        self.recovery_page.open_recovery_page()
        self.recovery_page.go_to_password_recovery()
 
        assert self.recovery_page.is_recovery_page()

    @allure.title('Ввод почты и клик по кнопке "Восстановить" открывает форму нового пароля')
    def test_enter_email_and_click_recovery_button(self):
       
        self.recovery_page.open()
        self.recovery_page.recover_password()
        assert self.recovery_page.is_new_password_form_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле пароля активным')
    def test_click_show_hide_password_button_makes_password_field_active(self):
        
        self.recovery_page.open()
        self.recovery_page.recover_password()
        
        self.recovery_page.toggle_password_visibility()
    
        assert self.recovery_page.is_password_field_active()
