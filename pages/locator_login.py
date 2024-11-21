from selenium.webdriver.common.by import By


class Locator_Login:

    # Locator by ID, XPATH, CSS dll
    email_id = (By.ID, "email")
    password_id = (By.ID, "password")
    btn_submit_id = (By.ID, "submitLoginBtn")