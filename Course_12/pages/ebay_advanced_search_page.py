from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page


class Advanced_search_page(Base_page):

    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID, "_nkw")
    KEYWORD_OPTIONS = (By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
    EXCLUDE_WORDS_FROM_SEARCH = (By.ID, "_ex_kw")
    SEARCH_CATEGORIES = (By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    SEARCH_BUTTON = (By.XPATH, '//span[@class="adv-keywords__help"]//parent::div//child::button')

    def enter_keywords_or_item_number(self, ):
        self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys("Pampers")

    def select_keywords_options(self):
        keyword_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
        keyword_dropdown.select_by_visible_text("Exact words, any order")

    def exclude_words_from_search(self):
        self.chrome.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys("")

    def select_search_category(self):
        keyword_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        keyword_dropdown.select_by_visible_text("Baby")

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()