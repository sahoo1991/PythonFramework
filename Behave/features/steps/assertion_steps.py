import time

from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from Behave.lib.pages.google_home.google_search_results import GoogleSearchResults

use_step_matcher("re")

@then('user should see some results populated')
def verify_google_search_results(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = GoogleSearchResults(context)

    try:
        wait.until(EC.visibility_of_element_located(page.search_results))
        element_found = True
    except:
        element_found = False
    msg = "no search results found..!!"
    assert element_found, msg


@then('user should see the gmail inbox page')
def verify_gmail_inbox_page(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = GoogleSearchResults(context)
    try:
        wait.until(EC.visibility_of_element_located(page.gmail_compose_button))
        element_found = True
    except:
        element_found = False
    msg = "Gmail inbox not found..!!"
    assert element_found, msg


@then('user should see google image home page')
def verify_image_home_page(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = GoogleSearchResults(context)
    try:
        wait.until(EC.visibility_of_element_located(page.google_image_home_page))
        element_found = True
    except:
        element_found = False
    msg = "Google image home page not found..!!"
    assert element_found, msg