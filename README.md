# Sales Store Automated Framework (Educational Exercise)

Welcome to the Sales Store Automated Framework. This project is designed as an educational exercise for building and understanding automated testing frameworks using Selenium with a strong focus on maintainability and scalability through the Page Object Model (POM) design pattern.

Disclaimer: This project is for educational purposes only and is not intended for production use. It was created as a learning exercise to demonstrate key automation testing techniques.

Table of Contents
Project Overview
Technologies Used
Project Structure
Installation and Setup
Running Tests
Contributing
Project Overview
This project provides an automated testing framework for a hypothetical sales store web application. It automates various user flows such as searching for products, adding products to the cart, and proceeding to checkout. The project adopts the Page Object Model (POM) pattern to enhance test maintainability, readability, and scalability.

The main goals of this project are:

To automate core functionalities of a web-based store for learning purposes.
To utilize best practices in test automation.
To make the tests easy to maintain and extend with the POM pattern.
Note: This project is part of an educational exercise and is not representative of a real-world application or production environment.

Technologies Used
The following technologies and libraries are used in this project:

Python: The programming language used to develop the test framework.
Selenium WebDriver: Used to automate browser interactions.
PyTest: A testing framework to run and manage the tests.
WebDriver Manager: Automatically handles the download and setup of web drivers.
Page Object Model (POM): A design pattern used to model the pages of the web application as classes, improving code reusability and maintainability.
PyTest HTML Reports: Generate detailed test reports in HTML format.
Project Structure
The project follows a modular structure to separate concerns and enhance readability:

plaintext
Copy code
.
├── pages/                # Page Objects for each page in the application
│   ├── home_page.py      # HomePage class handling search functionality
│   ├── product_page.py   # ProductPage class handling product details and actions
│   └── __init__.py       # Init file for the pages package
├── tests/                # Test cases
│   ├── test_search_bar.py # Tests for the search functionality
│   ├── test_buy_smart_tv.py # Tests for buying smart TVs
│   └── __init__.py       # Init file for the tests package
├── utils/                # Utility files such as browser setup
│   └── browser_setup.py  # Browser setup file handling WebDriver
├── config/               # Configuration files
│   └── config.py         # Configurations like base URL, timeouts, etc.
├── reports/              # Folder to store HTML reports
├── requirements.txt      # Dependencies for the project
└── README.md             # This README file
Page Object Model (POM)
The Page Object Model (POM) is used to represent the web pages of the application as objects. Each page object contains methods to interact with elements on the page, abstracting the complexity of selectors and making tests more readable and maintainable.

Example:

HomePage: Contains methods for interacting with the search bar, search button, and typeahead suggestions.
ProductPage: Contains methods to interact with product details, add items to the cart, and proceed to checkout.
Installation and Setup
To get started with this project, follow these steps:

1. Clone the Repository
bash
Copy code
git clone https://github.com/PonchoAlpha00/Sales_store_automated_framework.git
cd Sales_store_automated_framework
2. Set Up a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install the Dependencies
bash
Copy code
pip install -r requirements.txt
4. WebDriver Setup
The WebDriver Manager is used to automatically handle the download and setup of the browser drivers (e.g., ChromeDriver). No manual setup is required.

Running Tests
To run the tests, use the following command:

bash
Copy code
pytest
Generating HTML Reports
To generate HTML reports of the test runs, use the following command:

bash
Copy code
pytest --html=reports/report.html --self-contained-html
Running Specific Tests
You can also run a specific test or a group of tests using markers. For example, to run smoke tests:

bash
Copy code
pytest -m "smoke"
Contributing
Contributions are welcome! If you’d like to contribute, please fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License.
