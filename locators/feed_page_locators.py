from selenium.webdriver.common.by import By


class FeedLocators:
  
    ORDER_CARDS = (By.XPATH,"//li[contains(@class,'OrderHistory_listItem') or contains(@class,'OrderHistory_item')]")

    FIRST_ORDER_CARD = (By.XPATH,"(//li[contains(@class,'OrderHistory_listItem') or contains(@class,'OrderHistory_item')])[1]")
    ORDER_MODAL = (By.XPATH,"//section[contains(@class,'Modal_modal_opened')]")
    ORDER_MODAL_NUMBER = (By.XPATH,"//section[contains(@class,'Modal_modal_opened')]//p[contains(@class,'text_type_digits-default')]")
    MODAL_CLOSE_BUTTON = (By.XPATH,"//button[contains(@class,'Modal_modal__close')]")

    TOTAL_DONE_COUNTER = (By.XPATH,"//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_DONE_COUNTER = ((By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text.text_type_digits-large"))

  
    IN_PROGRESS_SECTION = (By.XPATH,"//ul[contains(@class,'OrderFeed_orderListReady')]")
    IN_PROGRESS_NUMBERS = (By.XPATH,"//ul[contains(@class,'OrderFeed_orderListReady')]//li")
    ALL_ORDER_NUMBERS = (By.XPATH,"//li[contains(@class,'OrderHistory_listItem') or contains(@class,'OrderHistory_item')]//p[contains(@class,'text_type_digits-default')]")   
