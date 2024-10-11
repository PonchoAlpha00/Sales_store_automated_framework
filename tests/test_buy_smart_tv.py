import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.product_description import ProductDescriptionPage
from utils.browser_setup import BrowserSetup
from selenium.webdriver.support.ui import WebDriverWait
from config.config import Config

@pytest.fixture(scope="class")
def setup_browser(request):
    driver = BrowserSetup().setup_browser()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup_browser")
class TestShoppingFlows:
    
    @pytest.mark.smoke
    def test_add_to_cart_and_proceed_to_checkout(self):
        # Step 1: Navigate to the base URL
        self.driver.get(Config.BASE_URL)
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        product_description = ProductDescriptionPage(self.driver)

        search_term = "Smart TV"

        # Step 2: Search for 'Smart TV'
        home_page.enter_search_text(search_term)
        home_page.click_search_button()

        # Step 3: Select the first Smart TV product from the search results
        selected_product_name = product_page.select_first_product_from_results()

        # Step 4: Validate product name and price on the product description page
        product_name = product_description.get_product_name()
        regular_price, discount_price = product_description.get_product_price()

        print(f"Product selected: {product_name}, Regular Price: {regular_price}, Discounted Price: {discount_price}")

        # Step 5: Get the initial cart count
        initial_cart_count = product_description.get_cart_count()
        print(f"Initial cart count: {initial_cart_count}")
         
        # Step 6: Add the product to the cart
        product_description.add_to_cart()

        # Step 6: Proceed to the cart after adding the product
        product_description.proceed_to_cart()

        # Step 7: Wait for the cart count to update
        WebDriverWait(self.driver, 10).until(
            lambda driver: product_description.get_cart_count() > initial_cart_count
        )

        # Step 8: Capture updated cart count
        updated_cart_count = product_description.get_cart_count()
        print(f"Updated cart count: {updated_cart_count}")

        # Step 9: Assert that the cart count has increased by 1
        assert updated_cart_count == initial_cart_count + 1, f"Expected cart count to increase by 1. Initial: {initial_cart_count}, Updated: {updated_cart_count}"

        # Step 10: Proceed to the cart after adding the product
        product_description.proceed_to_cart()

        # Step 11: Validate that the user lands on the checkout page by checking the URL
        expected_checkout_url = "https://www.liverpool.com.mx/tienda/oneCheckout"
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.current_url == expected_checkout_url
        )

        # Assert that the user is redirected to the correct checkout page
        assert self.driver.current_url == expected_checkout_url, f"Expected URL {expected_checkout_url} but got {self.driver.current_url}"


    @pytest.mark.smoke
    def test_buy_smart_tv_with_buy_now(self):
        # Navigate to the base URL
        self.driver.get(Config.BASE_URL)
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        product_description = ProductDescriptionPage(self.driver)

        search_term = "Smart TV"

        # Step 1: Search for 'Smart TV'
        home_page.enter_search_text(search_term)
        home_page.click_search_button()

        # Step 2: Select the first Smart TV product from the search results
        selected_product_name = product_page.select_first_product_from_results()

        # Step 3: Validate product name and price on the product description page
        product_name = product_description.get_product_name()
        regular_price, discount_price = product_description.get_product_price()

        print(f"Product selected: {product_name}, Regular Price: {regular_price}, Discounted Price: {discount_price}")

        # Step 4: Click the 'Buy Now' button to proceed directly to checkout
        product_description.buy_now()


        # Step 5: Validate that the user lands on the checkout page by checking the URL
        expected_checkout_url = "https://www.liverpool.com.mx/tienda/oneCheckout"
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.current_url == expected_checkout_url
        )

        # Assert that the user is redirected to the correct checkout page
        assert self.driver.current_url == expected_checkout_url, f"Expected URL {expected_checkout_url} but got {self.driver.current_url}"
