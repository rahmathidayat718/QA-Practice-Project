import time
from pages.ecommerce.add_to_cart_page import AddToCart
from pages.ecommerce.login_ecommerce_page import LoginEcommercePage
from testcases.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class TestAddToCart:

    logger = Log_Maker.log_gen()

    def test_add_to_cart(self, driver, config_data):
        login_page = LoginEcommercePage(driver)
        driver.get(config_data["login_url_page"])
        add_to_cart_page = AddToCart(driver)

        # Login
        email, password = Read_Config.get_data_login()
        login_page.login_ecommerce(email, password)

        # Add To Cart
        add_to_cart_page.test_add_to_cart()
        time.sleep(3)

        # Validation
        add_to_cart_page.validation()

