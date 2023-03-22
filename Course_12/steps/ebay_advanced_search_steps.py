from behave import *

@when('Advanced search page: I type Pampers in the text box')
def step_impl(context):
    context.advanced_search_object.enter_keywords_or_item_number()

@when('Advanced search page: I select Exact words, exact order from dropdown list')
def step_impl(context):
    context.advanced_search_object.select_keywords_options()

@when('Advanced search page: I select Baby from the category list')
def step_impl(context):
    context.advanced_search_object.select_search_category()

@when('Advanced search page: I click search button')
def step_impl(context):
    context.advanced_search_object.click_search_button()