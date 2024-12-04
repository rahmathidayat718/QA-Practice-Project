import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Test data
LOGIN_URL = "https://qa-practice.netlify.app/auth_ecommerce"
VALID_EMAIL = "admin@admin.com"
VALID_PASSWORD = "admin123"
DASHBOARD_TEXT = "Welcome to the Ecommerce"


@pytest.fixture(scope="function")
def driver():
    # Setup Chrome WebDriver
    options = Options()
    options.add_argument("--headless")  # Uncomment if you want to run tests in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_success(driver):
    # Navigate to the login page
    driver.get(LOGIN_URL)

    # Locate email, password fields, and login button
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    # Input valid email and password
    email_field.send_keys(VALID_EMAIL)
    password_field.send_keys(VALID_PASSWORD)
    login_button.click()

    # Validate successful login by checking the dashboard text
    dashboard_message = driver.find_element(By.TAG_NAME, "h1").text
    assert DASHBOARD_TEXT in dashboard_message, f"Expected '{DASHBOARD_TEXT}', got '{dashboard_message}'"
