import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from page_object.base_page import BasePage
from page_object.login_page import LoginPage
from page_object.register_page import RegisterPage
from data.url import URL_BURGER_MAIN
from data.user_data import generate_user_data

from locators.main_page_locators import MainLocators
from locators.profile_page_locators import ProfileLocators


class TestPersonalAccount:

    @pytest.fixture(params=["chrome", "firefox"], autouse=True)
    def setup_browser(self, request):
        browser_name = request.param

        if browser_name == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_name == "firefox":
            self.driver = webdriver.Firefox()

        self.wait = WebDriverWait(self.driver, 10)
        self.user_data = generate_user_data()

        yield

        self.driver.quit()

    def register_and_login_user(self):
        register_page = RegisterPage(self.driver)
        login_page = LoginPage(self.driver)

        register_page.register(
            self.user_data["name"],
            self.user_data["email"],
            self.user_data["password"]
        )

        login_page.submit_login(
            self.user_data["email"],
            self.user_data["password"]
        )

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_click_personal_account_opens_profile(self):
        self.driver.get(URL_BURGER_MAIN)
        base_page = BasePage(self.driver)

        base_page.wait_for_element(MainLocators.LOGO_SVG)
        self.register_and_login_user()

        base_page.click_element(MainLocators.PERSONAL_ACCOUNT_LINK)

        assert "account" in self.driver.current_url

    @allure.title('Переход в раздел "История заказов"')
    def test_click_order_history_opens_history_page(self):
        self.driver.get(URL_BURGER_MAIN)
        base_page = BasePage(self.driver)

        base_page.wait_for_element(MainLocators.LOGO_SVG)
        self.register_and_login_user()

        base_page.click_element(MainLocators.PERSONAL_ACCOUNT_LINK)
        base_page.wait_for_visible_element(ProfileLocators.ORDER_HISTORY_LINK)
        base_page.click_element(ProfileLocators.ORDER_HISTORY_LINK)

        assert "order-history" in self.driver.current_url

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self):
        self.driver.get(URL_BURGER_MAIN)
        base_page = BasePage(self.driver)

        base_page.wait_for_element(MainLocators.LOGO_SVG)
        self.register_and_login_user()

        base_page.click_element(MainLocators.PERSONAL_ACCOUNT_LINK)
        base_page.wait_for_visible_element(ProfileLocators.LOGOUT_BUTTON)
        base_page.click_element(ProfileLocators.LOGOUT_BUTTON)
        base_page.wait_for_element(MainLocators.LOGIN_HEADER)

        assert "login" in self.driver.current_url
