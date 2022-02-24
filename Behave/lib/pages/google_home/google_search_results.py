from selenium.webdriver.common.by import By
from Behave.lib.pages.google_home.google_home_page import GoogleHomePage

class GoogleSearchResults(GoogleHomePage):
    def __init__(self, context=None):
        super(GoogleSearchResults, self).__init__(context=context)
        self.search_results = (By.XPATH, "//div[@id='tvcap']")
        self.gmail_compose_button = (By.XPATH, "//span[text()='Create an account']")
        self.google_image_home_page = (By.XPATH, " //img[@alt='Google Images']")