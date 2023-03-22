"""
Aici scriem instrctiuni cu care instantiem browserul
Vom avea 2 metode: before_all si after_all
"""
from TA33.BDD.pages.ebay_advanced_search_page import Advanced_search_page
from TA33.BDD.pages.ebay_hompage import Home_page
from browser import Browser

# urmeaza niste instructiuni pe care le executam inainte de toate testele
# before_all este o metoda care este recunoscuta de libraria behave si care se va executa inainte de toate testele

def before_all(context):  # context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
    context.browser = Browser() # definim un nou obiect al clasei Browser
    # acest browser va fi accesibil prin intermediul variabilei context
    context.home_page_object = Home_page()  # cream o instanta a clasei Home_page
    context.advanced_search_object = Advanced_search_page()

# after-all este o metoda care este recunoscuta de libraria behave si care se va executa dupa toate testele
def after_all(context):
    context.browser.close() # apelam metoda close din clasa Browser pe baza obiectului instantiat anterior
