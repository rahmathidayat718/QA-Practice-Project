from selenium.webdriver.common.by import By


class Locator_Login:

    # Locator by ID, XPATH, CSS dll
    email_id = (By.ID, "email")
    password_id = (By.ID, "password")
    btn_submit_xpath = (By.XPATH, '//*[@id="submitLoginBtn"]')
    ecommerce_title = (By.ID, "home")
    error_incorrect = (By.XPATH, '//*[@id="message"]')
    error_empty_password = (By.XPATH, '//*[@id="message"]')
    error_empty_username = (By.XPATH, '//*[@id="message"]')

class LocatorAddToCart:
    # Locator AddToCart
    handphone_element = (By.XPATH, '//*[@id="prooood"]/section[2]/div/div[4]/span')
    add_handphone1 = (By.XPATH, '//*[@id="prooood"]/section[2]/div/div[4]/div/button')
    add_handphone2 = (By.XPATH, '//*[@id="prooood"]/section[2]/div/div[5]/div/button')
    validasi_hp1 = (By.XPATH, '//*[@id="prooood"]/section[1]/div[2]/div[1]/div[1]/span')
    validasi_hp2 = (By.XPATH, '//*[@id="prooood"]/section[1]/div[2]/div[2]/div[1]/span')