import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(params=["chrome", "firefox"], autouse=True)
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)

    yield driver

    driver.quit()

