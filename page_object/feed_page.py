import allure

from page_object.base_page import BasePage
from locators.feed_page_locators import FeedLocators
from locators.main_page_locators import MainLocators
from locators.feed_page_locators import FeedLocators

from page_object.base_page import BasePage
from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait

from data.url import URL_FEED
from data.user_data import TEST_EMAIL, TEST_PASSWORD

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #@allure.step('Открываем ленту заказов')        
    #def open_feed_page(self):
        #self.driver.get(URL_FEED)

    @allure.step('Ожидаем видимость пераого заказа')
    def wait_for_visible_first_order(self):
        self.wait_for_visible_element(FeedLocators.FIRST_ORDER_CARD)
    
    @allure.step('Открыть первую карточку заказа в ленте')
    def open_first_order(self):
        self.click_element(FeedLocators.FIRST_ORDER_CARD)

    @allure.step("Ожидание видимости модального окна")
    def wait_for_visible_order_modal(self):
        self.wait_for_visible_element(FeedLocators.ORDER_MODAL)

    @allure.step('Ищем модальное окно')
    def find_order_modal(self):
        return self.find_element(FeedLocators.ORDER_MODAL)

    @allure.step('Получить номер заказа из модалки')
    def get_order_number_from_modal(self):
        return self.get_text(FeedLocators.ORDER_MODAL_NUMBER)

    @allure.step('Получить счётчик "Выполнено за все время"')
    def get_total_done_count(self):
        return int(self.get_text(FeedLocators.TOTAL_DONE_COUNTER))

    @allure.step('Получить счётчик "Выполнено за сегодня"')
    def get_today_done_count(self):
        return int(self.get_text(FeedLocators.TODAY_DONE_COUNTER))

    @allure.step('Получить номера заказов из блока "В работе"')
    def get_in_progress_numbers(self):
        elements = self.find_elements(FeedLocators.IN_PROGRESS_NUMBERS)
        return [el.text.strip() for el in elements if el.text.strip()]
    
    @allure.step('Логин пользователя с тестовымит данными')
    def login_user(self):
        login_page = LoginPage(self.driver)  
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

    def normalize_order_number(order_number):
            return order_number.replace("#", "").lstrip("0")
    
    @allure.step('Создание заказа и получение его номера')
    def create_order_and_get_number(self):
            self.wait_for_visible_element(MainLocators.LOGO_SVG)
            
            login_page = LoginPage(self.driver)
            login_page.login(TEST_EMAIL, TEST_PASSWORD)

            main_page = MainPage(self.driver)
            
            main_page.create_order()
            
            self.wait_for_visible_element(MainLocators.ORDER_MODAL)
            self.wait_for_element(MainLocators.ORDER_NUMBER)
            
            order_number = self.get_text(MainLocators.ORDER_NUMBER)
            order_number = order_number.replace("#", "").lstrip("0")
            
            main_page.close_modal()
            self.wait_for_invisible_element(MainLocators.ORDER_MODAL)
            
            return order_number
    
    @allure.step("Проверяем наличие заказа на странице 'Лента заказов'")
    def is_order_in_feed(self, order_number, timeout=120):
        WebDriverWait(self.driver, timeout).until(
                lambda d: order_number in [
                    el.text.replace("#", "").lstrip("0")
                    for el in d.find_elements(*FeedLocators.ALL_ORDER_NUMBERS)
                ]
            )
        return True
    
    @allure.step('Открываем ленту заказов') 
    def open(self):
        self.driver.get(URL_FEED)
        self.wait_for_visible_element(FeedLocators.TOTAL_DONE_COUNTER)

    @allure.step("Ждем изменения счетчика 'Выполнено за все время'")
    def wait_for_total_done_increase(self, before_count, timeout=120):
        def total_done_increased(driver):
            current = int(driver.find_element(*FeedLocators.TOTAL_DONE_COUNTER).text)
            return current > before_count
    
        WebDriverWait(self.driver, timeout).until(total_done_increased)
        return self.get_total_done_count()
    

    @allure.step("Ждем изменения счетчика 'Выполнено за сегодня'")
    def wait_for_today_done_increase(self, before_count, timeout=120):
        def today_done_increased(driver):
            current = int(driver.find_element(*FeedLocators.TODAY_DONE_COUNTER).text)
            return current > before_count
        
        WebDriverWait(self.driver, timeout).until(today_done_increased)
        return self.get_today_done_count()
    
    @allure.step("Ждем появления раздела 'В работе' и получаем номер")
    def is_order_in_progress(self, order_number, timeout=120):
        self.wait_for_visible_element(FeedLocators.IN_PROGRESS_SECTION)
       
        WebDriverWait(self.driver, timeout).until(
            lambda d: order_number in self._get_normalized_in_progress_numbers(d)
        )

        in_progress_numbers = self.get_in_progress_numbers()
        normalized_numbers = [num.replace("#", "").lstrip("0") for num in in_progress_numbers]
        
        return order_number in normalized_numbers
    
    @allure.step("Приводим номер заказа к нрмальному числу")
    def _get_normalized_in_progress_numbers(self, driver):
        elements = driver.find_elements(*FeedLocators.IN_PROGRESS_NUMBERS)
        return [el.text.replace("#", "").lstrip("0") for el in elements]

    @allure.step("Открываем ленту заказов с главной страницы")
    def open_from_main_page(self):
        self.click_element(MainLocators.FEED_LINK)

    @allure.step('Проверка что пользователь находится на странице "Лента заказов"')
    def is_feed_page(self):
        return URL_FEED in self.driver.current_url
