"""
Aproape fiecare element de pe un site are un element tip clasa
Daca avem o clasa care contine spatiu, de fapt avem 2 clase.
Fiecare clasa este separata prin spatiu
Cum se cauta o clasa pentru a vedea daca este unica? --> CTRL + F -> [class="value"]
Cand facem cautare dupa class name, vom face cautarea fie dupa una sau cealalta
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://the-internet.herokuapp.com/login")

# maximizam fereastra
chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)