from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDescriptionPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for product description page elements
        self.product_name_locator = (By.CSS_SELECTOR, "h1.a-product__information--title")
        self.regular_price_locator = (By.CSS_SELECTOR, "p.a-product__paragraphRegularPrice")
        self.discount_price_locator = (By.CSS_SELECTOR, "p.a-product__paragraphDiscountPrice")
        self.quantity_input_locator = (By.ID, "a-stickyBarPdp__inputQty")
        self.add_to_cart_button = (By.ID, "opc_pdp_addCartButton")  # Add to Cart button
        self.buy_now_button = (By.ID, "opc_pdp_buyNowButton")  # Buy Now button
        self.cart_count_locator = (By.CSS_SELECTOR, "button.a-header__bag span")


    def get_product_name(self):
        product_name_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_name_locator)
        )
        return product_name_element.text.strip()

    def get_product_price(self):
        regular_price_element = self.driver.find_element(*self.regular_price_locator)
        discount_price_element = self.driver.find_element(*self.discount_price_locator)
        
        regular_price = regular_price_element.text.strip()
        discount_price = discount_price_element.text.strip()

        return regular_price, discount_price

    def set_product_quantity(self, quantity):
        quantity_input = self.driver.find_element(*self.quantity_input_locator)
        quantity_input.clear()  # Clear existing value
        quantity_input.send_keys(str(quantity))  # Set new quantity

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def buy_now(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.buy_now_button)
        ).click()
    
    def get_cart_count (self):
        cart_count = int(self.driver.find_element(*self.cart_count_locator).text.strip())
    
        return cart_count
    
