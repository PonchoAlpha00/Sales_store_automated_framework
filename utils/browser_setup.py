# utils/browser_setup.py

from selenium import webdriver
from config.config import Config
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class BrowserSetup:
    def setup_browser(self):
        if Config.BROWSER == "chrome":
            # Chrome browser options
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=2500,2500")  # Set window size
            #options.add_argument("--headless=new")           # Run headless mode with latest headless behavior
            options.add_argument("--incognito")              # Open in incognito mode
            
            # Use Service to handle WebDriver executable installation (Selenium 4)
            service = webdriver.chrome.service.Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        else:
            raise ValueError(f"Browser '{Config.BROWSER}' is not supported.")

        # Set base URL and wait times from config
        driver.get(Config.BASE_URL)
        driver.implicitly_wait(Config.IMPLICIT_WAIT)  # Set implicit wait
        return driver
