import allure

from page_object.base_page import BasePage
from locators.main_page_locators import MainLocators
from data.url import URL_BURGER_MAIN
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть вкладку Конструктор')
    def open_constructor(self):
        self.click_element(MainLocators.CONSTRUCTOR_LINK)

    @allure.step('Открыть вкладку Лента заказов')
    def open_feed(self):
        self.click_element(MainLocators.FEED_LINK)

    @allure.step('Открыть модалку деталей ингредиента')
    def open_ingredient_details(self):
        self.click_element(MainLocators.BUN_CRATER_CARD)

    @allure.step('Закрыть модалку')
    def close_modal(self):
        self.click_element_js(MainLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Добавить булку в конструктор')
    def add_bun_to_constructor(self):
        self.drag_and_drop(
            MainLocators.BUN_CRATER_CARD,
            MainLocators.CONSTRUCTOR_DROP_AREA
        )

    @allure.step('Получить значение каунтера булки')
    def get_bun_counter(self):
        return self.get_text(MainLocators.BUN_CRATER_COUNTER)

    @allure.step('Нажать кнопку Оформить заказ')
    def click_order_button(self):
        self.click_element(MainLocators.ORDER_BUTTON)

    @allure.step('Создать заказ')
    def create_order(self):
        self.add_bun_to_constructor()
        self.click_order_button()
        self.wait_for_visible_element(MainLocators.ORDER_MODAL)
        self.wait_for_element(MainLocators.ORDER_NUMBER)
        return self.get_text(MainLocators.ORDER_NUMBER)
    
    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(URL_BURGER_MAIN)
        self.wait_for_visible_element(MainLocators.LOGO_SVG)

    @allure.step('Проверка, тчо пользователь на главной странице')
    def is_main_page(self):
        return self.driver.current_url == URL_BURGER_MAIN

    @allure.step('Проверка, что модальное окно с деталями по ингридиентам отображается')
    def is_ingredient_modal_displayed(self):
        return self.find_element(MainLocators.INGREDIENT_DETAILS_MODAL).is_displayed()

    @allure.step("Закрыть модальное окно подробной информации")
    def close_ingredient_modal(self):
        self.click_element(MainLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверка, что модальное окно закрылось")
    def is_ingredient_modal_closed(self):
        return self.wait_for_invisible_element(MainLocators.INGREDIENT_DETAILS_MODAL)
    
    @allure.step("Получение значения из каунтера булки")
    def get_bun_counter_value(self):
        counters = self.find_elements(MainLocators.BUN_COUNTER)
        return 0 if not counters else int(counters[0].text)

    @allure.step("Ожидание изменения каунтера булки")
    def wait_for_bun_counter_increase(self, before_count, timeout=10):
        def counter_increased(driver):
            counters = driver.find_elements(*MainLocators.BUN_COUNTER)
            if not counters:
                return False
            return int(counters[0].text) > before_count
        
        WebDriverWait(self.driver, timeout).until(counter_increased)
        return self.get_bun_counter_value()
        



        
