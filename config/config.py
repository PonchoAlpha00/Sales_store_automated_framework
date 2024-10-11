# config/config.py

class Config:
    # Base URL for the application under test
    BASE_URL = "https://www.liverpool.com.mx/tienda/home"

    # Browser type (can be extended to support other browsers like Firefox)
    BROWSER = "chrome"  # Options: "chrome", "firefox"

    # Implicit and explicit wait times (in seconds)
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20

    # Credentials (if you want to store login data for certain tests)
    USERNAME = "test_user"
    PASSWORD = "secure_password"

    # Paths for report output or downloads (can be useful for some tests)
    REPORT_PATH = "./reports/"
    DOWNLOAD_PATH = "./downloads/"
