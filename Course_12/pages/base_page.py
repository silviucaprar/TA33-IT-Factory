from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser
"""
clasa asta trebuie sa mosteneasca clasa Browser ca sa avem acces la el
cum inca nu stim de ce avem nevoie, ii punem pass
daca ne trebuie vreo metoda de care avem nevoie in mai multe pagini, o sa le scriem aici 
"""

class Base_page(Browser):

    COOKIES_BUTTON = (By.ID, "gdpr-banner-accept")

    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.COOKIES_BUTTON).click()
        except:
            pass

    def wait_and_click_element_by_selector(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
        self.chrome.find_element(by, selector).click()