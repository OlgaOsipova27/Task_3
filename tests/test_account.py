import allure
import pytest

from page_object.main_page import MainPage
from page_object.profile_page import ProfilePage
from page_object.user_page import UserPage 
from page_object.login_page import LoginPage


class TestPersonalAccount:

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.main_page = MainPage(driver)
        self.profile_page = ProfilePage(driver)
        self.user_page = UserPage(driver)
        self.login_page = LoginPage(driver)

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_click_personal_account_opens_profile(self):
        self.main_page.open()
        user_data = self.user_page.get_test_user_data()
        self.login_page.login(user_data["email"],
        user_data["password"])
        self.profile_page.open_from_main_page()
        assert self.profile_page.is_profile_page()

    @allure.title('Переход в раздел "История заказов"')
    def test_click_order_history_opens_history_page(self):
        self.main_page.open()
        user_data = self.user_page.get_test_user_data()
        self.login_page.login(user_data["email"],
        user_data["password"])
        
        self.main_page.open()
        self.profile_page.open_from_main_page()
        self.profile_page.go_to_order_history()
        
        assert self.profile_page.is_order_history_page()

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self):
        self.main_page.open()
        user_data = self.user_page.get_test_user_data()
        self.login_page.login(user_data["email"],
        user_data["password"])
        
        self.main_page.open()
        self.profile_page.open_from_main_page()
        self.profile_page.logout()
        
        assert self.profile_page.is_login_page()
