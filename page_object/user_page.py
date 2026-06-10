import allure
from page_object.register_page import RegisterPage
from page_object.login_page import LoginPage


class UserPage:
    def __init__(self, driver):
        self.driver = driver
        self.register_page = RegisterPage(driver)
        self.login_page = LoginPage(driver)
    
    @allure.step("Зарегистрировать пользователя и авторизоваться")
    def register_and_login(self, name, email, password):
        self.register_page.register(name, email, password)
        self.login_page.login(email, password)
    
    @allure.step("Получить тестовые данные пользователя")
    def get_test_user_data(self):
        return {
            "name": "testtest",
            "email": "test_user2@yandex.ru",
            "password": "password1234"
        }
