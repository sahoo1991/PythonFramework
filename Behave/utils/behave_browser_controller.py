from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# This file is getting called by environment.py file from before scenario section
class BrowserController:
    def __init__(self, context, browser_type, use_grid):
        self.port = 4444
        self.context = context
        self.useGrid = use_grid
        self.driver = self.InvokeBrowser(browser_type)
        # This is the clean up method
        context.add_cleanup(self.driver.quit)

    def InvokeBrowser(self, browser_name):
        if browser_name == "chrome":
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_argument("start-maximized")
            chromeOptions.add_argument("--ignore-certificate-errors")
            chromeOptions.add_argument("--disable-features=RendererCodeIntegrity")
            capabilities = chromeOptions.to_capabilities()
            self.driver = webdriver.Remote("http://localhost:" + str(self.port) + "/wd/hub",
                                           desired_capabilities=capabilities)
            self.driver.delete_all_cookies()
            self.driver.maximize_window()
            return self.driver
        elif browser_name == "mobile":
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.prompt_for_download": False}
            chromeOptions.add_experimental_option("prefs", prefs)
            chromeOptions.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
            chromeOptions.add_argument("start-maximized")
            chromeOptions.add_argument("--ignore-certificate-errors")
            chromeOptions.add_argument("--disable-features=RendererCodeIntegrity")
            capabilities = chromeOptions.to_capabilities()
            self.driver = webdriver.Remote("http://localhost:" + str(self.port) + "/wd/hub", desired_capabilities=capabilities)
            self.driver.delete_all_cookies()
            self.driver.maximize_window()
            return self.driver
        else:
            options = webdriver.IeOptions()
            options.ensure_clean_session = True
            options.ignore_zoom_level = True
            self.driver = webdriver.Remote("http://localhost:" + str(self.port) + "/wd/hub",
                                           options=options)
            self.driver.maximize_window()
            return self.driver
