from selenium.webdriver.common.by import By


class Locator_Login:

    # Locator by ID, XPATH, CSS dll
    email_id = (By.ID, "email")
    password_id = (By.ID, "password")
    btn_submit_id = (By.ID, "submitLoginBtn")
    ecommerce_title = (By.ID, "home")
    error_incorrect = (By.XPATH, '//*[@id="message"]')
    error_empty_password = (By.XPATH, '//*[@id="message"]')
    error_empty_username = (By.XPATH, '//*[@id="message"]')