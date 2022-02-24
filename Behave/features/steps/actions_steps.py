import time

from behave import given, when, then
from Behave.lib.pages.google_home.google_home_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium.webdriver.common.keys import Keys

use_step_matcher("re")

@given('the user opens google')
def open_google_website(context):
    context.browser.driver.get("https://www.google.co.in")


@when('the user searches with the string (.*)')
def search_in_google(context, search_string):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = GoogleHomePage(context)

    msg = "google search field not displayed"
    search_field = wait.until(EC.element_to_be_clickable(page.google_search_field), msg)
    search_field.send_keys(search_string)
    search_field.send_keys(Keys.ENTER)


@when('the user clicks the gmail link')
def click_gmail_link(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=2, poll_frequency=0.5)
    page = GoogleHomePage(context)

    msg = "Gmail link not displayed"
    wait.until(EC.element_to_be_clickable(page.gmail_link), msg).click()


@when('the user clicks the image link on the home page')
def click_image_link(context):
    driver = context.browser.driver
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = GoogleHomePage(context)

    msg = "Image link not displayed"
    wait.until(EC.element_to_be_clickable(page.image_link), msg).click()