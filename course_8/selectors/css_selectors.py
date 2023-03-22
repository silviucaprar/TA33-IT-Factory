"""
studiu individual : https://www.w3schools.com/cssref/css_selectors.php

Cum sa gandim un selector?

# -> cautare dupa id
. -> cautare dupa clasa
daca precedm # sau . de numele unui tag, atunci sistemul va cauta elementele cu tag-ul respectiv si id-ul/clasa respectiva
Putem sa cautam elemente cu un anumit tag cu filtrare de tipul atribut = valoare
Putem sa cautam primul copil al unui element cu caracterul >
Putem sa cautam orice copil al unui element daca separam tag-ul prin spatiu
Daca vrem sa cautam primul copil al unui element putem sa specificam first-of-type
Daca vrem sa cautam ultimul copil al unui element putem sa specificam last-of-type
Daca vrem sa cautam un copil care nu este nici primul nici ultimul, putem sa folosim nth-of-type(al catelea element este)
Daca vrem sa gasim un frate ulterior, ne putem folosi de caracterul +
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select



chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://the-internet.herokuapp.com/")
chrome.implicitly_wait(10)

# maximizam fereastra
chrome.maximize_window()
time.sleep(1)

# get element by id
# tagname[attribute=value]
chrome.find_element(By.PARTIAL_LINK_TEXT, "Form ").click()
chrome.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
# putem folosi si syntaxa input[id=username]
chrome.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
time.sleep(2)

# get element by class
# tagname.class_name or input[class=value]
# chrome.find_element(By.CSS_SELECTOR, "button.radius").click()
# button.radius[type='submit']
time.sleep(2)



"""
sub strings - good for dynamic elements
^ prefixul textului
syntax: tagname[attribute^='prefix']
$ - sufixul textului
syntax: tagname[attribute$='sufix']
* sub-stringul textului 
syntax: tagname[attribute*='sub_string']
"""

# prefix
# chrome.find_element(By.CSS_SELECTOR, "button.radius[type^='sub']").click()

# sufix
# chrome.find_element(By.CSS_SELECTOR,"button.radius[type$='mit']").click()


#substring
# chrome.find_element(By.CSS_SELECTOR, "button.radius[type*='bm']").click()
time.sleep(2)

"""
childs
> select direct child
tagname[attribute='value']>tagname[attribute='value']
"""
# div[id=ajaxPage1]>div

chrome.back()

# treat dropdown
chrome.find_element(By.LINK_TEXT, "Dropdown").click()
dropdown_list = Select(chrome.find_element(By.CSS_SELECTOR, "select#dropdown"))
time.sleep(2)
dropdown_list.select_by_visible_text("Option 2")
time.sleep(2)

#   >:first-child
#   >:last-child
#   >:nth-child(2)
# select[id=dropdown]>:nth-child(3)

chrome.quit()

