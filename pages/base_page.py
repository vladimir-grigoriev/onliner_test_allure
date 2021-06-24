import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = 'https://www.onliner.by/'
    
    def go_to_site(self):
        self.driver.get(self.base_url)
    
    def find_element(self, locator, timeout=20):
        time.sleep(0.5)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def click_element(self, locator, timeout=30):
        time.sleep(1)
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def switch_to_iframe(self, locator, timeout=10):
        time.sleep(0.5)
        WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(locator),
            message=f"Can't find element by locator {locator}"
        )

    def element_send_keys(self, locator, text, timeout=10):
        time.sleep(0.5)
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)