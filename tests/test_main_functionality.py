import allure
import pytest

from page_object.main_page import MainPage
from page_object.feed_page import FeedPage
from page_object.login_page import LoginPage
from page_object.user_page import UserPage

class TestMainFunctionality:

#так как тесты используют разные page objects оставила инициализацию отделно для каждого класса тестов (без фикстуры), а не вынесла в conftest
    def setup_pages(self, driver):
        self.main_page = MainPage(driver)
        self.feed_page = FeedPage(driver)
        self.login_page = LoginPage(driver)
        self.user_page = UserPage(driver)

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_opens_constructor_page(self):

        self.feed_page.open()
        self.main_page.open_constructor()

        assert self.main_page.is_main_page()

    @allure.title('Переход по клику на «Лента заказов» c главной страницы')
    def test_click_feed_opens_feed_page(self):

        self.main_page.open()
        self.feed_page.open_from_main_page()

        assert self.feed_page.is_feed_page()

    @allure.title('Клик по ингредиенту открывает модальное окно с деталями')
    def test_click_ingredient_opens_modal(self):
        
        self.main_page.open()
        self.main_page.open_ingredient_details()
        
        assert self.main_page.is_ingredient_modal_displayed()

    @allure.title('Модальное окно закрывается по клику на крестик')
    def test_modal_closes_after_click_close_button(self):
        
        self.main_page.open()
        
        self.main_page.open_ingredient_details()
        self.main_page.close_ingredient_modal()
       
        assert self.main_page.is_ingredient_modal_closed()

    @allure.title('При добавлении булки в заказ увеличивается каунтер ингредиента')
    def test_ingredient_counter_increases_after_adding_to_order(self):
        
        self.main_page.open()
        
        before_count = self.main_page.get_bun_counter_value()
        self.main_page.add_bun_to_constructor()
        after_count = self.main_page.wait_for_bun_counter_increase(before_count)
        
        assert after_count > before_count

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self):
        
        self.main_page.open()
        user_data = self.user_page.get_test_user_data()
       
        self.login_page.login(user_data["email"],
        user_data["password"])
        
        self.main_page.add_bun_to_constructor()
        order_number = self.main_page.create_order()
        
        assert order_number is not None
