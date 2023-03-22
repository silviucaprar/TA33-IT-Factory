import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Context_Menu(unittest.TestCase):

    BOX = (By.ID, "hot-spot")

    def setUp(self) -> None:
        # toate activitatile care trebuie sa fie executate inainte de orice test
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.get("https://the-internet.herokuapp.com/context_menu")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_context_menu(self):
        action = ActionChains(self.chrome)  # create ActionChains object
        elem = self.chrome.find_element(*self.BOX)
        action.context_click(elem).perform()
        time.sleep(3)
        self.chrome.switch_to.alert.accept()
        time.sleep(2)