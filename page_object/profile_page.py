import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
from data.url import URL_BURGER_MAIN

from page_object.base_page import BasePage
from locators.main_page_locators import MainLocators
from locators.profile_page_locators import ProfileLocators


class ProfilePage(BasePage):

    @allure.step("Открываем личный кабинет с главной страницы")
    def open(self):
       self.driver.get(URL_BURGER_MAIN)
       self.click_element(MainLocators.PERSONAL_ACCOUNT_LINK)
       self.wait_for_url_change("account")

    @allure.step("Ожидаем смену url")
    def wait_for_url_change(self, expected_part):
       WebDriverWait(self.driver, 10).until(
         lambda d: expected_part in d.current_url
       )

    @allure.step("Открытие старницы 'История заказов'")
    def go_to_order_history(self):
        self.click_element(ProfileLocators.ORDER_HISTORY_LINK)
        self.wait_for_visible_element(ProfileLocators.ALL_HISTORY_ORDER_NUMBERS)

    @allure.step('Проверяем, что номер заказа отобрадется в истории')
    def is_order_in_history(self, order_number):
        WebDriverWait(self.driver, 10).until(
            lambda d: order_number in [
                el.text.replace("#", "").lstrip("0")
                for el in d.find_elements(*ProfileLocators.ALL_HISTORY_ORDER_NUMBERS)
            ]
        )
        return True
    
    @allure.step("Открываем личный кабинет с главной страницы")
    def open_from_main_page(self):
        
        self.driver.get(URL_BURGER_MAIN)
        self.wait_for_visible_element(MainLocators.LOGO_SVG)

        self.click_element(MainLocators.PERSONAL_ACCOUNT_LINK)
        self.wait_for_url_change("account")

    @allure.step("Проверка, что пользователь на странице лисного кабинета")
    def is_profile_page(self):
        return "account" in self.driver.current_url

    @allure.step("Ожидание смены url")
    def wait_for_url_change(self, expected_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: expected_part in d.current_url
        )
        return True

    @allure.step("Переход на страницу исторрии заказов")
    def go_to_order_history(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ProfileLocators.ORDER_HISTORY_LINK)).click()
        self.wait_for_url_change("order-history")

    @allure.step("Проверка, что пользователь на странице истории заказов")
    def is_order_history_page(self):
        return "order-history" in self.driver.current_url

    @allure.step("Выход из аккаунта")
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainLocators.LOGIN_HEADER)
        )

    @allure.step("Проверка, что пользователь на странице истории заказов")
    def is_login_page(self):
        return "login" in self.driver.current_url
