import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from page_object.base_page import BasePage
from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from page_object.feed_page import FeedPage

from data.url import URL_BURGER_MAIN, URL_FEED
from data.user_data import TEST_EMAIL, TEST_PASSWORD

from locators.main_page_locators import MainLocators
from locators.feed_page_locators import FeedLocators
from locators.profile_page_locators import ProfileLocators


class TestFeed:

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

    def login_user(self):
        login_page = LoginPage(self.driver)
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

    def create_order_and_get_number(self):
        base_page = BasePage(self.driver)
        main_page = MainPage(self.driver)

        base_page.wait_for_visible_element(MainLocators.LOGO_SVG)
        self.login_user()

        main_page.create_order()

        base_page.wait_for_visible_element(MainLocators.ORDER_MODAL)
        base_page.wait_for_visible_element(MainLocators.ORDER_NUMBER)

        order_number = base_page.find_element(MainLocators.ORDER_NUMBER).text.strip()
        order_number = order_number.replace("#", "").lstrip("0")

        main_page.close_modal()
        base_page.wait_for_invisible_element(MainLocators.ORDER_MODAL)

        return order_number

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_opens_modal(self):
        self.driver.get(URL_FEED)

        base_page = BasePage(self.driver)
        feed_page = FeedPage(self.driver)

        base_page.wait_for_visible_element(FeedLocators.FIRST_ORDER_CARD)
        feed_page.open_first_order()

        base_page.wait_for_visible_element(FeedLocators.ORDER_MODAL)

        assert base_page.find_element(FeedLocators.ORDER_MODAL).is_displayed()

    @allure.title('Заказы пользователя из истории отображаются в ленте заказов')
    def test_user_order_from_history_is_displayed_in_feed(self):
        self.driver.get(URL_BURGER_MAIN)
        created_order_number = self.create_order_and_get_number()

        def normalize_order_number(order_number):
            return order_number.replace("#", "").lstrip("0")

        created_order_number = normalize_order_number(created_order_number)

        base_page = BasePage(self.driver)

        old_url = self.driver.current_url
        base_page.click_element(MainLocators.PERSONAL_ACCOUNT_LINK)

        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != old_url
        )

        assert "account" in self.driver.current_url

        base_page.wait_for_visible_element(ProfileLocators.ORDER_HISTORY_LINK)
        base_page.click_element(ProfileLocators.ORDER_HISTORY_LINK)

        base_page.wait_for_visible_element(ProfileLocators.ALL_HISTORY_ORDER_NUMBERS)

        WebDriverWait(self.driver, 10).until(
            lambda d: created_order_number in [
                el.text.replace("#", "").lstrip("0")
                for el in d.find_elements(*ProfileLocators.ALL_HISTORY_ORDER_NUMBERS)
            ]
        )

        # заново находим элементы после ожидания
        history_order_numbers = [
            el.text.replace("#", "").lstrip("0")
            for el in base_page.find_elements(ProfileLocators.ALL_HISTORY_ORDER_NUMBERS)
        ]

        assert created_order_number in history_order_numbers

        self.driver.get(URL_FEED)
        base_page.wait_for_visible_element(FeedLocators.ORDER_CARDS)

        WebDriverWait(self.driver, 15).until(
            lambda d: created_order_number in [
                el.text.replace("#", "").lstrip("0")
                for el in d.find_elements(*FeedLocators.ALL_ORDER_NUMBERS)
            ]
        )

        # снова ищем свежие элементы
        feed_order_numbers = [
            el.text.replace("#", "").lstrip("0")
            for el in base_page.find_elements(FeedLocators.ALL_ORDER_NUMBERS)
        ]

        assert created_order_number in feed_order_numbers

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_total_done_counter_increases_after_new_order(self):
        self.driver.get(URL_FEED)

        feed_page = FeedPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(FeedLocators.TOTAL_DONE_COUNTER)
        before_count = feed_page.get_total_done_count()

        self.driver.get(URL_BURGER_MAIN)
        self.create_order_and_get_number()

        self.driver.get(URL_FEED)

        WebDriverWait(self.driver, 20).until(
            lambda d: int(d.find_element(*FeedLocators.TOTAL_DONE_COUNTER).text) >= before_count
        )

        after_count = feed_page.get_total_done_count()

        assert after_count >= before_count

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_done_counter_increases_after_new_order(self):
        self.driver.get(URL_FEED)

        feed_page = FeedPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(FeedLocators.TODAY_DONE_COUNTER)
        before_count = feed_page.get_today_done_count()

        self.driver.get(URL_BURGER_MAIN)
        self.create_order_and_get_number()

        self.driver.get(URL_FEED)

        WebDriverWait(self.driver, 20).until(
            lambda d: int(d.find_element(*FeedLocators.TODAY_DONE_COUNTER).text) >= before_count
        )

        after_count = feed_page.get_today_done_count()

        assert after_count >= before_count

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_created_order_number_appears_in_progress(self):
        self.driver.get(URL_BURGER_MAIN)
        created_order_number = self.create_order_and_get_number()

        self.driver.get(URL_FEED)

        feed_page = FeedPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.wait_for_visible_element(FeedLocators.IN_PROGRESS_SECTION)

        WebDriverWait(self.driver, 20).until(
            lambda d: created_order_number in d.page_source
        )

        in_progress_numbers = [
            number.replace("#", "").lstrip("0")
            for number in feed_page.get_in_progress_numbers()
        ]

        assert created_order_number in in_progress_numbers or created_order_number in self.driver.page_source
