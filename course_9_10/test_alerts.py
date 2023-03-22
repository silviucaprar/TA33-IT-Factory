"""
Libraria unittest este o librarie care suporta crearea de teste rulabile direct in interiorul clasei
Se implementeaza prin mostenirea clasei TestCAse din libraria unittest
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati
1. Metoda setup -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva
2. Metoda teardown -> toate activitatile care trebuie sa fie executate dupa ORICE TEST din clasa respectiva
3. toate metodele de test trebuie sa aiba prefixul test_
Metode de rulare:
1. Click dreapta pe fisier + Run
2. Din terminal
2.1. click dreapta pe numele pachetului (TREBUIE SA FIE PACHET) -> Copy Path / Reference -> Absolute Path
2.2. cd <calea pe care ati copiat-o>
2.3. pytest nume_fisier_de_rulat
instalare pytest: pip install pytest
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Alerts(unittest.TestCase):

    # definim constantele/variabile
    JS_ALERT_BUTTON = (By.XPATH, '//*[text()="Click for JS Alert"]')
    JS_CONFIRM_BUTTON = (By.XPATH, '//*[text()="Click for JS Confirm"]')
    JS_PROMPT_BUTTON = (By.XPATH, '//*[text()="Click for JS Prompt"]')
    ALERT_ACTION_MESSAGE = (By.ID, "result")
    INSERT_TEXT = "This is a test"

    #metoda de setup
    def setUp(self) -> None:
        # toate activitatile care trebuie sa fie executate inainte de orice test
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        # activitatile executate dupa terminarea testului
        self.chrome.quit()

    # de aici incepem sa scriem metodele
    def test_js_alert_accept(self):
        self.chrome.find_element(*self.JS_ALERT_BUTTON).click()
        # steluta are functie de despachetare a tuplului
        # metoda find_element asteapta doi parametrii: metoda de cautare, valoare
        # daca nu scriem *, atunci metoda va primi un singur parametru de tip tupla
        js_alert = self.chrome.switch_to.alert
        js_alert.accept()
        js_alert_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You successfully clicked an alert"
        self.assertEqual(expected_text, js_alert_text, f"ERROR: Expected {expected_text}, Actual: {js_alert_text}")

    def test_js_confirm_accept_alert(self):
        self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()
        js_confirm_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You clicked: Ok"
        self.assertEqual(expected_text, js_confirm_text, f"ERROR: expected {expected_text}, actual: {js_confirm_text}")

    def test_js_confirm_cancel_alert(self):
        self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
        js_cancel = self.chrome.switch_to.alert
        js_cancel.dismiss()
        js_cancel_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You clicked: Cancel"
        self.assertEqual(expected_text, js_cancel_text, f"ERROR: expected {expected_text}, actual: {js_cancel_text}")


    def test_js_prompt_accept_alert_with_text(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.send_keys(self.INSERT_TEXT)
        js_prompt.accept()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = f"You entered: {self.INSERT_TEXT}"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR: expected {expected_text}, actual: {js_prompt_text}")


    def test_js_prompt_accept_alert_without_text(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.accept()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You entered:"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR: expected {expected_text}, actual: {js_prompt_text}")

    # scenariu testare negativa
    # testare negativa = testarea situatiilor nefavorabile pe care sistemul ar trebui sa nu le poata executa, dar sa le trateze corect
    def test_js_prompt_cancel_alert_with_text(self):
        # gasim elementul button "Click for JS PROMPT" si dam click.
        # Path-ul unde se gaseste este declarat la inceputul clasei in costanta JS_PROMPT_BUTTON
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        # mergem pe alerta
        js_prompt = self.chrome.switch_to.alert
        #inseram un text. ne folosim de constanta INSERT_TEXT care contine textul "This is a test"
        js_prompt.send_keys(self.INSERT_TEXT)
        # dam cancel la alerta
        js_prompt.dismiss()
        #declaram o variabila in care stocam textul din elementul ALERT_ACTION_MESSAGE
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        # declaram o variabila in care stocam textul care ne asteptam sa il afiseze
        expected_text = "You entered: null"
        # comparam output cu expected result (js_prompt_text cu expected_text)
        self.assertEqual(expected_text, js_prompt_text, f"ERROR: expected {expected_text}, actual: {js_prompt_text}")

    def test_js_prompt_cancel_alert_without_text(self):
        self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.dismiss()
        js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
        expected_text = "You entered: null"
        self.assertEqual(expected_text, js_prompt_text, f"ERROR: expected {expected_text}, actual: {js_prompt_text}")





