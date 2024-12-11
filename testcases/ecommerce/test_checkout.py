import time
from venv import logger

from pages.ecommerce.add_to_cart_page import AddToCart
from pages.ecommerce.checkout_page import CheckoutPage
from pages.ecommerce.login_ecommerce_page import LoginEcommercePage
from testcases.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities.excel_reader import ExcelReader


class TestCheckout:

    logger = Log_Maker.log_gen()

    def test_add_to_cart(self, driver, config_data):
        login_page = LoginEcommercePage(driver)
        driver.get(config_data["login_url_page"])
        add_to_cart_page = AddToCart(driver)
        checkout = CheckoutPage(driver)

        # Login
        email, password = Read_Config.get_data_login()
        login_page.login_ecommerce(email, password)

        # Add To Cart
        add_to_cart_page.test_add_to_cart()
        time.sleep(3)

        # Validation
        add_to_cart_page.validation()

        # Checkout
        checkout.checkout_item()

        # Details
        excel_reader = ExcelReader("testdata/qa-practice-automation.xlsx")
        test_data = excel_reader.get_data(sheet_name="submit_order")
        for phone_number, street, city, country, Exp_result in test_data:
            checkout.submit_order(phone_number, street, city, country)

        #validasi
        checkout.validation_submit()