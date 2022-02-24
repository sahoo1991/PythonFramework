from selenium.webdriver.common.by import By


class GoogleHomePage(object):
    def __init__(self, context=None):
        self.google_search_field = (By.XPATH, "//input[@name='q']")
        self.google_search_button = (By.XPATH, "( //input[@aria-label='Google Search'])[2]")
        self.gmail_link = (By.XPATH, "//a[text()='Gmail']")
        self.image_link = (By.XPATH, "//a[@class='gb_d' and text() = 'Images']")
