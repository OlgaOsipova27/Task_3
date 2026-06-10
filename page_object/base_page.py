from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
 
from data.url import URL_BURGER_MAIN
from locators.main_page_locators import MainLocators

 
class BasePage:
    def __init__(self, browser):
        self.driver = browser

    def open_main_page(self):
        self.driver.get(URL_BURGER_MAIN)
 
    def wait_for_element(self, locator, timeout=100):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
 
    def open(self):
        self.driver.get(URL_BURGER_MAIN)
        self.wait_for_visible_element(MainLocators.LOGO_SVG)

    def wait_for_visible_element(self, locator, timeout=10):
  
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

 
    def wait_for_invisible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
 
    def get_url_new_tab(self, locator, timeout=10):
        old_tabs = len(self.driver.window_handles)
        self.click_element(locator)
 
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > old_tabs
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
 
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != "about:blank"
        )
        return self.driver.current_url
 
    def get_url_same_tab(self, locator, timeout=10):
        old_url = self.driver.current_url
        self.click_element(locator)
 
        WebDriverWait(self.driver, timeout).until(
            EC.url_changes(old_url)
        )
        return self.driver.current_url
 
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
 
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        self.scroll_to_element(element)
        ActionChains(self.driver).move_to_element(element).click().perform()
 
    def click_element_js(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
 
    def fill_input(self, locator, text):
        element = self.wait_for_visible_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(text)
 
    def find_element(self, locator):
        return self.driver.find_element(*locator)
 
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
 
    def get_text(self, locator):
        return self.find_element(locator).text

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_visible_element(source_locator)
        target = self.wait_for_visible_element(target_locator)

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            const dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragStartEvent);

            const dragEnterEvent = new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragEnterEvent);

            const dragOverEvent = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragEndEvent);
            """,
            source,
            target
        )
