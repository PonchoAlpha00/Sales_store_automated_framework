import pytest
from utils.browser_setup import BrowserSetup
from config.config import Config

@pytest.fixture(scope="class")
def setup_browser(request):
    # Setup the browser
    driver = BrowserSetup().setup_browser()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup_browser")
class TestBrowserSetup:
    
    def test_browser_launch(self):
        # Open the base URL and assert the page title
        self.driver.get(Config.BASE_URL)
        assert "Liverpool" in self.driver.title, "Page title does not contain 'Liverpool'."
