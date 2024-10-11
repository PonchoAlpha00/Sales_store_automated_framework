from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Apply implicit wait globally for all element searches
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)

        self.search_result = (By.XPATH, "//li[contains(@class,'active')]")

        # Filter selectors
        self.brand_filter_title = (By.XPATH, "//label[contains(@class_title,'Marcas')]")
        self.brand_filter_selector = "//label[contains(text(), '{}')]"

        self.size_filter_title = (By.XPATH, "//label[contains(@class_title,'Tamaño')]")
        self.size_filter_selector = "//label[contains(text(), '{}')]"

        self.price_filter_title = (By.XPATH, "//label[contains(@class_title,'Precios')]")
        self.price_filter_selector = "//label[contains(text(), '{}')]"

        self.breadcrumb_locator = (By.XPATH, "//div[@class='m-breadcrumb']//li[@class='active']//strong")
        self.product_count_locator = (By.XPATH, "//p[contains(@class,'a-plp-results-title')]/span")

        self.product_card_locator = (By.CSS_SELECTOR, "li.m-product__card")
        self.product_name_locator = (By.CSS_SELECTOR, "h3.card-title")
        self.product_price_locator = (By.CSS_SELECTOR, "p.a-card-price")
        self.product_link_locator = (By.CSS_SELECTOR, "a")
        self.add_to_cart_button = (By.XPATH, "//button[contains(@class,'add-to-cart')]")  # Update based on actual HTML
        self.cart_button = (By.XPATH, "//button[contains(@class,'go-to-cart')]")  # Button to proceed to cart
        self.cart_product_title = (By.XPATH, "//div[@class='cart-product-title']")  # Product title in the cart


    def click_price_radio_button_by_label_text(self, label_text):
        # Format the class variable XPath template with the label_text
        xpath = self.price_filter_selector.format(label_text)

        # Find the label element for the price filter
        label = self.driver.find_element(By.XPATH, xpath)
        
        # Navigate to the parent div and find the associated radio button
        parent_div = label.find_element(By.XPATH, "..")
        radio_button = parent_div.find_element(By.CSS_SELECTOR, "input[type='radio']")

        # Click the radio button
        radio_button.click()

        # Optional: Confirm the radio button is now selected
        if not radio_button.is_selected():
            raise Exception(f"Failed to select the radio button associated with label '{label_text}'.")

    def click_brand_checkbox_by_label_text(self, label_text):
        # Format the class variable XPath template with the label_text
        xpath = self.brand_filter_selector.format(label_text)

        # Find the label element for the brand filter
        label = self.driver.find_element(By.XPATH, xpath)

        # Navigate to the parent div and find the associated checkbox
        parent_div = label.find_element(By.XPATH, "..")
        checkbox = parent_div.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

        # Click the checkbox
        checkbox.click()

        # Optional: Confirm the checkbox is now selected
        if not checkbox.is_selected():
            raise Exception(f"Failed to select the checkbox associated with label '{label_text}'.")

    def click_size_checkbox_by_label_text(self, label_text):
        # Format the class variable XPath template with the label_text
        xpath = self.size_filter_selector.format(label_text)

        # Find the label element for the size filter
        label = self.driver.find_element(By.XPATH, xpath)

        # Navigate to the parent div and find the associated checkbox
        parent_div = label.find_element(By.XPATH, "..")
        checkbox = parent_div.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

        # Click the checkbox
        checkbox.click()

        # Optional: Confirm the checkbox is now selected
        if not checkbox.is_selected():
            raise Exception(f"Failed to select the checkbox associated with label '{label_text}'.")
    
    def read_breadcrumb(self):

        breadcrumb_element = self.driver.find_element(By.XPATH, self.breadcrumb_locator)
        breadcrumb_text = breadcrumb_element.text.lower()

        return breadcrumb_text
    
    def get_product_count(self):

        # Find the <span> element inside the <p> and extract the text
        product_count_element = self.driver.find_element(*self.product_count_locator)
        product_count_text = product_count_element.text.strip()  # Extract the text and remove any surrounding whitespace
        
        try:
            # Convert the text to an integer
            product_count = int(product_count_text)
            print(f"Number of products found: {product_count}")
            return product_count
        except ValueError:
            raise Exception(f"Failed to convert the product count text '{product_count_text}' to an integer.")

    def select_first_product_from_results(self):
        # Wait until the product cards are visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_card_locator)
        )

        # Get all product cards
        product_cards = self.driver.find_elements(*self.product_card_locator)

        # Get the first product card
        first_product = product_cards[0]
        
        # Extract the product name and price for logging or validation
        product_name = first_product.find_element(*self.product_name_locator).text.strip()
        product_price = first_product.find_element(*self.product_price_locator).text.strip()

        print(f"Selected Product: {product_name}, Price: {product_price}")

        # Click the first product link to navigate to its details page
        product_link = first_product.find_element(*self.product_link_locator)
        product_link.click()

        return product_name

    def add_to_cart(self):
    
        # Wait for the 'Add to Cart' button to be clickable, then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def proceed_to_checkout(self):
        
        # Wait for the 'Go to Cart' button to be clickable, then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        ).click()

    def validate_product_in_cart(self, expected_product_name):
        """
        Validate that the expected product is present in the shopping cart.
        
        :param expected_product_name: The name of the product to validate.
        :return: True if the product is found, otherwise raises an assertion error.
        """
        cart_product_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_product_title)
        )
        actual_product_name = cart_product_element.text.strip()
        assert expected_product_name.lower() in actual_product_name.lower(), f"Expected product '{expected_product_name}' not found in cart."