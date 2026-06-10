from selenium.webdriver.common.by import By


class ProfileLocators:
    PROFILE_LINK = (By.XPATH,"//a[@href='/account' and normalize-space()='Профиль']")

    ORDER_HISTORY_LINK = (By.XPATH,"//a[@href='/account/order-history' and normalize-space()='История заказов']")

    LOGOUT_BUTTON = (By.XPATH,"//button[normalize-space()='Выход']")

    FIRST_HISTORY_ORDER_NUMBER = (By.XPATH,"((//li[contains(@class,'OrderHistory_listItem') or contains(@class,'OrderHistory_item')])//p[contains(@class,'text_type_digits-default')])[1]")
    ALL_HISTORY_ORDER_NUMBERS = (By.XPATH,"//li[contains(@class,'OrderHistory_listItem') or contains(@class,'OrderHistory_item')]//p[contains(@class,'text_type_digits-default')]")
