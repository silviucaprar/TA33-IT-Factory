import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Hover_Elem(unittest.TestCase):

    CLOSE_BUTTON = (By.XPATH, "//a[@id='promoModalNLSubscribe_close']//child::span")
    ACCEPT_COOKIES = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    AROMA = (By.XPATH, "//nav[@id ='mainMenuBar']/ul/li[2]/a")

    def setUp(self) -> None:
        # toate activitatile care trebuie sa fie executate inainte de orice test
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.get("https://www.sabon.ro")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()


    def test_hover_over_arome(self):
        # inchide fereastra cu abonare
        # self.chrome.find_element(*self.CLOSE_BUTTON).click()
        # time.sleep(2)
        self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        elem = self.chrome.find_element(*self.AROMA)
        action = ActionChains(self.chrome).move_to_element(elem).perform()
        time.sleep(3)



