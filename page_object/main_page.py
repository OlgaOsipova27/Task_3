import allure

from page_object.base_page import BasePage
from locators.main_page_locators import MainLocators


class MainPage(BasePage):

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
