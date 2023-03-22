"""
Deschide o fereastra de chrome si navigati catre https://the-internet.herokuapp.com
Accesati pagina “Shifting Content” si selectati “Example 3: List”
Accesati pagina Checkboxes si deselectati “checkbox2” si selectati “checkbox1”
Accesati pagina “Inputs” si scrieti in Number text field, numarul “2222”
Printati “Yes I made it”

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# cream un nou obiect chrome al clasei Chrome din libraria webdriver
chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
chrome.maximize_window()

# navigam catre link
chrome.get("https://the-internet.herokuapp.com")
time.sleep(2)

# # cautam "Shifting Content" dupa text link (inspect element)
# chrome.find_element(By.LINK_TEXT, "Shifting Content").click()
# time.sleep(2)
#
# # selectam  “Example 3: List”
#
# chrome.find_element(By.LINK_TEXT, "Example 3: List").click()
# time.sleep(2)
#
# # mergem 2 pagini inapoi ca sa putem accesa Checkboxes
# # chrome.back()
# # chrome.back()
# chrome.execute_script("window.history.go(-2)")
# time.sleep(2)

# Acesam pagina Checkboxes cu Link Text
chrome.find_element(By.LINK_TEXT, "Checkboxes").click()
time.sleep(2)

# deselctam checkbox 2
input_list = chrome.find_elements(By.TAG_NAME, "input")
input_list[1].click()
time.sleep(2)

# selectam checkbox 1
input_list[0].click()
time.sleep(2)

# dam back sa ajungem la pagina principala
chrome.back()

# accesam Inputs page
chrome.find_element(By.LINK_TEXT, "Inputs").click()
time.sleep(2)

# scriem 2222 si folosim TAG_NAME
chrome.find_element(By.TAG_NAME, "input").send_keys("2222")
time.sleep(2)
print("Yes I made it!")