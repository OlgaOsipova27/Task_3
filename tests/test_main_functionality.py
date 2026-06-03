import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from page_object.base_page import BasePage
from page_object.login_page import LoginPage
from page_object.main_page import MainPage

from data.url import URL_BURGER_MAIN, URL_FEED
from data.user_data import TEST_EMAIL, TEST_PASSWORD

from locators.main_page_locators import MainLocators


class TestMainFunctionality:

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

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_opens_constructor_page(self):
        self.driver.get(URL_FEED)

        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(MainLocators.FEED_LINK)
        main_page.open_constructor()

        assert self.driver.current_url == URL_BURGER_MAIN

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_feed_opens_feed_page(self):
        self.driver.get(URL_BURGER_MAIN)

        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)
        main_page.open_feed()

        assert URL_FEED in self.driver.current_url

    @allure.title('Клик по ингредиенту открывает модальное окно с деталями')
    def test_click_ingredient_opens_modal(self):
        self.driver.get(URL_BURGER_MAIN)

        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)
        main_page.open_ingredient_details()

        base_page.wait_for_visible_element(MainLocators.INGREDIENT_DETAILS_HEADER)

        assert base_page.find_element(MainLocators.INGREDIENT_DETAILS_MODAL).is_displayed()

    @allure.title('Модальное окно закрывается по клику на крестик')
    def test_modal_closes_after_click_close_button(self):
        self.driver.get(URL_BURGER_MAIN)

        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)
        main_page.open_ingredient_details()
        base_page.wait_for_visible_element(MainLocators.INGREDIENT_DETAILS_HEADER)

        main_page.close_modal()

        assert base_page.wait_for_invisible_element(MainLocators.INGREDIENT_DETAILS_MODAL)

    @allure.title('При добавлении булки в заказ увеличивается каунтер ингредиента')
    def test_ingredient_counter_increases_after_adding_to_order(self):
        self.driver.get(URL_BURGER_MAIN)

        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)

        counters_before = base_page.find_elements(MainLocators.BUN_CRATER_COUNTER)
        before_count = 0 if not counters_before else int(counters_before[0].text)

        main_page.add_bun_to_constructor()

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*MainLocators.BUN_CRATER_COUNTER)) > 0 and
            int(d.find_element(*MainLocators.BUN_CRATER_COUNTER).text) > before_count
        )

        after_count = int(base_page.find_element(MainLocators.BUN_CRATER_COUNTER).text)

        assert after_count > before_count

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self):
        self.driver.get(URL_BURGER_MAIN)

        base_page = BasePage(self.driver)
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        main_page.add_bun_to_constructor()
        main_page.click_order_button()

        base_page.wait_for_visible_element(MainLocators.ORDER_MODAL)
        base_page.wait_for_visible_element(MainLocators.ORDER_NUMBER)

        assert base_page.find_element(MainLocators.ORDER_NUMBER).is_displayed()
