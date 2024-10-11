# Sales Store Automated Framework (Educational Exercise)

This project is designed as an **educational exercise** for building an automated testing framework using **Selenium** and the **Page Object Model (POM)** design pattern. It automates core functionalities of an online store, including searching for products, adding them to the cart, and proceeding to checkout.

> **Disclaimer**: This project is for **educational purposes** only.

---

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following to set up the project:

- **Python 3.x**: The programming language used to build the framework.
- **pip**: Python package manager (usually comes with Python).
- **Virtual Environment**: Recommended to isolate dependencies.
- **Git**: For version control and cloning the repository.

#### Example:

Install Python 3.x from the official [Python website](https://www.python.org/downloads/).

To install pip and virtual environment:

```bash
pip install virtualenv
```

### Installing

A step-by-step series of instructions to get a development environment running:

#### 1. Clone the repository:

```bash
git clone https://github.com/PonchoAlpha00/Sales_store_automated_framework.git
cd Sales_store_automated_framework
```

#### 2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### 4. Set up the browser drivers:

The WebDriver Manager is used to automatically handle the browser driver setup. No additional steps are required for Chrome/Firefox drivers.

### Finished Setup

After following these steps, your environment will be ready to run the automated tests included in this project.

---

## Project Structure

This project follows a well-structured, modular design to separate the various concerns in automated testing. Here’s an overview of the directory structure:

```plaintext
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
```

### Explanation of Key Components:

1. **Page Objects (POM)**: 
   - The **Page Object Model (POM)** design pattern is used to encapsulate all the elements and actions for each page. This improves the maintainability of tests by separating the logic for interacting with the page elements from the tests themselves.
   
   - **pages/** directory contains page classes like `home_page.py` and `product_page.py`, which model specific pages of the web application.

2. **Test Cases**:
   - **tests/** directory contains the actual test cases, which use the methods defined in the Page Object classes to interact with the web application. Each test focuses on a specific functionality (e.g., searching for products, adding items to the cart).

3. **Utility Classes**:
   - The **utils/browser_setup.py** contains the logic for setting up the browser (e.g., ChromeDriver), including configuration for headless mode and browser options.

4. **Configuration**:
   - **config/config.py** contains configuration settings such as base URLs, implicit wait times, and browser options. These can be easily adjusted based on the environment or requirements.

---

## Running the Tests

To run the automated tests for this system, use the following steps.

### End-to-End Tests

These tests simulate user interactions with the sales store web application, such as searching for products, adding items to the cart, and proceeding to checkout.

#### Example:

To run all tests:

```bash
pytest
```

To generate an HTML report of the test run:

```bash
pytest --html=reports/report.html --self-contained-html
```

### Coding Style Tests

The framework follows **PEP 8** coding standards. You can run linting tools like `flake8` to ensure the code adheres to these standards.

#### Example:

To install `flake8` and run the style checks:

```bash
pip install flake8
flake8 .
```

---

## Deployment

This project is intended for educational purposes and local execution only. There are no instructions for deploying it on a live system, as it is not a production-ready application.

---

## Built With

- **Selenium WebDriver** - Browser automation tool.
- **PyTest** - Framework for writing and running tests.
- **WebDriver Manager** - Handles automatic driver management.
- **Page Object Model (POM)** - Design pattern used for structuring the project.
- **PyTest HTML Reports** - For generating HTML reports of test results.

---

## Contributing

If you wish to contribute, please fork the repository, create a new branch, and submit a pull request.

---

## Versioning

This project does not follow a specific versioning system. It is meant for educational purposes. However, you may implement versioning if necessary using [SemVer](http://semver.org/).

---

## Authors

- **Alfonso Armando Perez Cerda** - Initial work for this educational project.

See the list of [contributors](https://github.com/PonchoAlpha00/Sales_store_automated_framework/graphs/contributors) who participated in this project.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---

## Acknowledgments

- Thanks to the creators of the tools used in this project.
- Hat tip to the open-source community for providing resources and support.

---
