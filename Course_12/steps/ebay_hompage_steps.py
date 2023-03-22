"""
features -> features : scenarios
pages -> definite metodele
clasele din pages mostenesc base page
dupa ce am creat pagina, mergem in environment si instatiam un obiect de tip page-ul(class) pe care l-am creat
"""
from behave import *

@given('Home page: I am on ebay homepage')
    # se va duce in feature si va cauta un pas in care sa gaseasca exact descrierea asta
def step_impl(context): # context esre recunoscut ca un element din fisierul environment si o sa ne putem folosi de el
    context.home_page_object.navigate_to_homepage()
    context.home_page_object.accept_cookies()

@when('Home page: I search for "{product_name}" from category "{category_name}"')
def step_impl(context, product_name, category_name):
    context.home_page_object.insert_search_value(product_name)
    context.home_page_object.choose_category(category_name)
    context.home_page_object.click_search_button()

# @then('I received as results also iPhone8 64Gb')
# def step_impl(context):
#     context.home_page_object.check_search_results()

@when('Home page: I click on the advanced link')
def step_impl(context):
    context.home_page_object.click_advanced_search_link()

