import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pages import page1


class TestPage1(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def tearDown(self) -> None:
        self.driver.quit()

    def test_input(self):
        self.page = page1.Page1(self.driver)
        self.page.go_to_site()
        self.page.set_an_item_to_search_field("Iphone")
        self.page.choose_first_item_in_list()
        first_item_price = self.page.get_first_item_price()
        self.page.click_at_first_element()
        first_item_card_price = self.page.get_price_from_card()
        self.assertEqual(first_item_price, first_item_card_price)
