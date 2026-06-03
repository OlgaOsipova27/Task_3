import allure

from page_object.base_page import BasePage
from locators.feed_page_locators import FeedLocators


class FeedPage(BasePage):

    @allure.step('Открыть первую карточку заказа в ленте')
    def open_first_order(self):
        self.click_element(FeedLocators.FIRST_ORDER_CARD)

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
