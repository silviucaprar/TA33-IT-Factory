from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page


class Home_page(Base_page):

    SEARCH_TEXTBOX = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")
    SEARCH_CATEGORIES = (By.ID, "gh-cat")
    ADVANCED_SEARCH_LINK = (By.ID, "gh-as-a")
    HOMEPAGE_LINK = "https://www.ebay.com/"
    SEARCH_RESULTS = (By.XPATH, '//span[text()="Apple iPhone 8 64GB 256GB 4G LTE iOS Smartphone Grey Silver Gold Red - Unlocked"]')

    def navigate_to_homepage(self):
        self.chrome.get(self.HOMEPAGE_LINK)

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(product_name)

    def choose_category(self, category_name):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category_name)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def click_advanced_search_link(self):
        self.wait_and_click_element_by_selector(*self.ADVANCED_SEARCH_LINK)

    # def check_search_results(self):
    #     self.chrome.find_element(*self.SEARCH_RESULTS)