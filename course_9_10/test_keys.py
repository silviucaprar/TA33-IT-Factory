import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Keyboard(unittest.TestCase):

    USERNAME = (By.ID, "username")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()


    def test_select_all(self):
        user = self.chrome.find_element(*self.USERNAME)
        user.send_keys("Miriam")
        time.sleep(2)
        # stergem continutul
        user.clear()
        time.sleep(1)
        user.send_keys("tosmih")
        time.sleep(2)
        # select all and del
        user.send_keys(Keys.CONTROL, 'a')
        user.send_keys(Keys.BACKSPACE)
        user.send_keys("tomsmith")
        time.sleep(2)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(3)