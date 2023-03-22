"""
Diferenta dintre Relative XPATH and Absolute XPATH:
Absolute XPATH:  contine calea completa incepand cu elementul radacina
Relative XPATH: incepe prin a preciza elementul la care vrei tu sa te duci

XPATH este folosit sa navigheze prin nodurile XML
Syntxa: //tagname[@Attribute='Value']
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By




chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://the-internet.herokuapp.com/key_presses")

# maximizam fereastra
chrome.maximize_window()
time.sleep(2)

# chrome.find_element(By.XPATH, '//*[@id="login"]/button').click()
# # calea relativa: //*[@id="login"]/button
# # calea absoluta: /html/body/div[2]/div/div/form/button

"""
Cum construim un XPATH?
1. Click dreapta pe elementul pe care vrem sa-l gasim -> inspect element
2. CTRL + F care deschide o fereastra mica de cautare jos
3. Cream XPATH-ul folosindu-ne de syntaxa
"""

# chrome.find_element(By.XPATH, "//input[@id='target']").send_keys("blab bla ")
# time.sleep(2)

chrome.find_element(By.XPATH, "//input[@id='target' and @type='text']").send_keys("blab bla ")
time.sleep(2)
"""
### XPATH AXES METHODS ####
pe unul sau mai multe noduri s-ar putea s anu existe atribute unice
atunci putem cauta un atribut unic in parinte si sa ne folosim de el pt a gasi elementul
axes = se refera la relatia dintre nodul curent si celelalte noduri

Xpath following-siblings
following: selecteaza toate nodurile care apar dupa nodul curent
Syntax: //tagname[@attribute='value']//following::tagname
"""
# example
chrome.find_element(By.XPATH, "//ul[@class='mainMenuList parent-1']//following::a")

"""
following-sibling: selecteaza toate nodurile care au acelasi parinte cu nodul curent si care apar dupa nodul curent
syntax: //tagname[@Attribute='Value']//following-sibling::tagname
i.e //tagname[@Attribute='Value']//following-sibling::tagname[@Atrribute='Value']
"""
chrome.find_element(By.XPATH, "//ul[@class='WbrtSideMenu has-grandchildren']//following::ul[@class='submenu-list']//following-sibling::li[2]")

"""
preceding: selecteaza toate nodurile care apar inainte de nodul curent
//tagname[@Attribute='Value']//preceding::tagname
"""
chrome.find_element(By.XPATH,  "//ul[@class='WbrtSideMenu has-grandchildren']//preceding::div")
# in cazul de mai sus, acceseaza primul div din pagina. daca vrem un anumit div, folosim parametrul [nr]


"""
preceding-sibling: selecteaza toate nodurile care au acelasi aprinte ca nodul curent si apar inainte de nodul curent
syntax: //tagname[@attribute='value']//preceding-sibling::tagname
"""

"""
parent: selecteaza parintele nodului curent
syntax: //tagname[@attribute='value']//parent::tagname
"""
chrome.find_element(By.XPATH, "//ul[@class='WbrtSideMenu has-grandchildren']//parent::div")
"""
child: selecteaza toti copiii nodului curent
syntax: //tagname[@attribute='value']//child::tagname
"""
chrome.find_element(By.XPATH, "//ul[@class='WbrtSideMenu has-grandchildren']//child::ul")

"""
self - selcteaza nodul curent
syntax: //tagname[@attribute='value']//self::tagname
"""


"""
starts with
este o functie ajutatoare daca vrem sa identificam elemente dinamice intr-o pagina web
- o putem folosi ca sa gasim valoarea de inceput a elementului care ramane static
syntax: //tagname[starts-with(@attribute, 'value')]
"""

chrome.find_element(By.XPATH, "//input[starts-with(@id, 'username_')]")

"""
ends with
este o functie ajutatoare daca vrem sa identificam elemente dinamice intr-o pagina web
- o putem folosi ca sa gasim valoarea de inceput a elementului care ramane static
syntax: //tagname[ends-with(@attribute, 'value')]
"""
chrome.find_element(By.XPATH, "//input[starts-with(@id, '_username')]")


"""
contains : putem sa ii dam orice valoare partiala a atributului ca sa gasim webelementul
syntax: //tagname[contains(@attribute, 'value')]
"""


"""
text() - este o metoda care va gasi un element dupa text
syntax: //tagname[text()='the_text']
"""
chrome.find_element(By.XPATH, "//label[text()='Username']")

