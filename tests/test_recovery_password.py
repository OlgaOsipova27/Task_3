import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from page_object.base_page import BasePage
from page_object.recovery_page import RecovPassPage
from data.url import URL_BURGER_MAIN, URL_FORGOT_PASS
from locators.main_page_locators import MainLocators, PasswordRecoveryLocators as passloc


class TestRecoveryPassword:

    @pytest.fixture(params=["chrome", "firefox"], autouse=True)
    def setup_browser(self, request):
        browser_name = request.param

        if browser_name == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_name == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        yield

        self.driver.quit()

    @allure.title('Переход по кнопке "Восстановить пароль" открывает страницу восстановления')
    def test_click_on_button_recovery_password_open_recovery_page(self):
        self.driver.get(URL_BURGER_MAIN)

        base_page = BasePage(self.driver)
        recovery_page = RecovPassPage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)
        recovery_page.open_login_page_login_button()

        url = base_page.get_url_same_tab(MainLocators.FORGOT_PASSWORD_LINK)

        assert url == URL_FORGOT_PASS

    @allure.title('Ввод почты и клик по кнопке "Восстановить" открывает форму нового пароля')
    def test_enter_email_and_click_recovery_button(self):
        self.driver.get(URL_FORGOT_PASS)

        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(passloc.PASSWORD_RECOVERY_HEADER)
        base_page.fill_input(passloc.INPUT_NAME, "test@yandex.ru")
        base_page.click_element(passloc.RECOVERY_BUTTON)

        base_page.wait_for_visible_element(passloc.NEW_PASSWORD_INPUT)

        assert base_page.find_element(passloc.NEW_PASSWORD_INPUT).is_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле пароля активным')
    def test_click_show_hide_password_button_makes_password_field_active(self):
        self.driver.get(URL_FORGOT_PASS)

        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(passloc.PASSWORD_RECOVERY_HEADER)
        base_page.fill_input(passloc.INPUT_NAME, "test@yandex.ru")
        base_page.click_element(passloc.RECOVERY_BUTTON)

        base_page.wait_for_visible_element(passloc.NEW_PASSWORD_INPUT)
        base_page.click_element(passloc.PASSWORD_SHOW_HIDE_BUTTON)

        container_class = base_page.find_element(
            passloc.PASSWORD_INPUT_CONTAINER
        ).get_attribute("class")

        assert "input_status_active" in container_class
