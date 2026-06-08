import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from page_object.base_page import BasePage
from page_object.profile_page import ProfilePage
from page_object.main_page import MainPage
from page_object.feed_page import FeedPage

from data.url import URL_BURGER_MAIN, URL_FEED
from data.user_data import TEST_EMAIL, TEST_PASSWORD

from locators.main_page_locators import MainLocators
from locators.feed_page_locators import FeedLocators
from locators.profile_page_locators import ProfileLocators


class TestFeed:

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.feed_page = FeedPage(driver)
        self.profile_page = ProfilePage(driver)


    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_opens_modal(self):
    
        self.feed_page.open()
        self.feed_page.wait_for_visible_first_order()
        self.feed_page.open_first_order()
        self.feed_page.wait_for_visible_order_modal()
        
        assert self.feed_page.find_order_modal().is_displayed()

    @allure.title('Заказы пользователя в истории заказов')
    def test_user_order_from_history_is_displayed_in_history(self):
        
        self.main_page.open()
        created_order_number = self.feed_page.create_order_and_get_number()

        self.profile_page.open()
        self.profile_page.go_to_order_history()
        assert self.profile_page.is_order_in_history(created_order_number)
        

    @allure.title('Заказы пользователя из истории отображаются в ленте заказов')
    def test_user_order_from_history_is_displayed_in_feed(self):
        
        self.main_page.open()
        created_order_number = self.feed_page.create_order_and_get_number()
   
        self.profile_page.open()
        self.profile_page.go_to_order_history()
        self.feed_page.open()
        assert self.feed_page.is_order_in_feed(created_order_number)


    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_total_done_counter_increases_after_new_order(self):

        self.feed_page.open()

        before_count = self.feed_page.get_total_done_count()

        self.main_page.open()
        self.feed_page.create_order_and_get_number()

        self.feed_page.open()

        after_count = self.feed_page.wait_for_total_done_increase(before_count)

        assert after_count > before_count


    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_done_counter_increases_after_new_order(self):

        self.feed_page.open()
        
        before_count = self.feed_page.get_today_done_count()

        self.main_page.open()
        self.feed_page.create_order_and_get_number()

        self.feed_page.open()
 
        after_count = self.feed_page.wait_for_today_done_increase(before_count)

        assert after_count > before_count


    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_created_order_number_appears_in_progress(self):
        
        self.main_page.open()
        created_order_number = self.feed_page.create_order_and_get_number()
        
        self.feed_page.open()
         
        assert self.feed_page.is_order_in_progress(created_order_number)
