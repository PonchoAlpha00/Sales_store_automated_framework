import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.browser_setup import BrowserSetup
from config.config import Config

# Define a pytest fixture to handle browser setup and teardown
@pytest.fixture(scope="class")
def setup_browser(request):
    # Setup the browser using the config
    driver = BrowserSetup().setup_browser()
    request.cls.driver = driver  # Attach driver to the class
    yield
    driver.quit()  # Teardown after test class finishes

@pytest.mark.usefixtures("setup_browser")
class TestSearchBar:
    
    # Test for searching a Smart TV
    @pytest.mark.smoke
    def test_search_smart_tv(self):
        # Navigate to the base URL
        self.driver.get(Config.BASE_URL)
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)

        search_term = "Smart TV"

        # Search for 'Smart TV' on the website
        home_page.enter_search_text(search_term)
        home_page.click_search_button()

        # Assert that the page title contains 'Smart TV'
        assert search_term.lower() in self.driver.title.lower(), f"'{search_term}' not found in page title after search."
        
        # Assert that the breadcrumb contains 'Smart TV'
        breadcrumb_text = product_page.read_breadcrumb()
        assert search_term.lower() in breadcrumb_text.lower(), f"'{search_term}' not found in breadcrumb after search."

        # Check that the product count is valid (greater than or equal to 0)
        product_count = product_page.get_product_count()
        assert product_count >= 0, f"Invalid product count: {product_count}"





