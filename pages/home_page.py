from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config  # Import your config

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Set the implicit wait globally based on the config
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)

        # Locators
        self.search_box = (By.XPATH, "//input[contains(@id,'mainSearchbar')]")  # Adjust the selector if necessary
        self.search_button = (By.XPATH, "//button[contains(@class,'input-group-text')]")
        self.typeahead_box = (By.CLASS_NAME, "m-typeahead")  # Typeahead suggestions container
        self.typeahead_suggestion = (By.CLASS_NAME, "a-sayt__typeaheadLink")  # Typeahead suggestion item (cards)


    def enter_search_text(self, text, retries=3, timeout=5):
        """
        Clicks on the search box, waits for typeahead suggestions to load, 
        enters search text one character at a time, waits to verify if the input remains, 
        and retries if the input is cleared.

        :param text: Text to be entered in the search bar.
        :param retries: Number of retries to attempt if the input gets cleared.
        :param timeout: Time to wait before checking if the input persists.
        """
        search_box_element = self.driver.find_element(*self.search_box)

        for attempt in range(retries):
            try:
                # Click on the search box to focus it
                search_box_element.click()

                # Wait for at least one suggestion card to appear (indicating the typeahead box is active)
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(self.typeahead_suggestion)
                )
                print(f"Typeahead suggestion card loaded on attempt {attempt + 1}.")

                # Enter the search text one character at a time
                search_box_element.clear()  # Clear any existing text
                for char in text:
                    search_box_element.send_keys(char)

                # Wait for a few seconds to check if the input persists
                WebDriverWait(self.driver, timeout).until(
                    lambda driver: driver.find_element(*self.search_box).get_attribute("value") == text
                )
                print(f"Search text '{text}' entered successfully on attempt {attempt + 1}.")
                return  # Exit the function if the input is successful

            except TimeoutException:
                print(f"Search text '{text}' was cleared or typeahead didn't load. Retrying... (Attempt {attempt + 1}/{retries})")

        # If the input keeps getting cleared after the retries, raise an exception or handle it
        raise Exception(f"Failed to enter search text '{text}' after {retries} retries.")

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()