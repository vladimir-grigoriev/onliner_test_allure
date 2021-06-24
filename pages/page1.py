import time
from selenium.webdriver.common.by import By

from .base_page import BasePage


class Page1Locators:
    INPUT = (By.CLASS_NAME, "fast-search__input")
    IFRAME = (By.CLASS_NAME, "modal-iframe")
    PRICE_FROM_IFRAME = (By.CSS_SELECTOR, ".product__price span")
    ELEMENT = (By.CSS_SELECTOR, ".result__wrapper a")
    PRICE_FROM_CARD = (By.CSS_SELECTOR, ".product-primary-i .offers-description .offers-description__details")


class Page1(BasePage):
    
    def set_an_item_to_search_field(self, text):
        self.element_send_keys(Page1Locators.INPUT, text)
    
    def choose_first_item_in_list(self):
        self.switch_to_iframe(Page1Locators.IFRAME)
    
    def get_first_item_price(self):
        return self.find_element(Page1Locators.PRICE_FROM_IFRAME).text
    
    def click_at_first_element(self):
        element = self.click_element(Page1Locators.ELEMENT)
        element.click()
        

    def get_price_from_card(self):
        time.sleep(5)
        return self.find_element(Page1Locators.PRICE_FROM_CARD).text.split("\n")[0]