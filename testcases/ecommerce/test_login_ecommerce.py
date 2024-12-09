
from pages.ecommerce.login_ecommerce_page import LoginEcommercePage
from utilities.excel_reader import ExcelReader
from utilities.custom_logger import Log_Maker
from venv import logger

class TestLoginEcommerce:

    logger = Log_Maker.log_gen()

    def test_ecommerce_login(self, driver, config_data):
        login_page = LoginEcommercePage(driver)

        # Read Data From Excel
        excel_reader = ExcelReader("testdata/qa-practice-automation.xlsx")
        test_data = excel_reader.get_data(sheet_name="Login")

        for email, password, status in test_data:
            driver.get(config_data["login_url_page"])
            login_page.login_ecommerce(email, password)

            # Validasi setelah login
            if status.lower() == "success":
                assert login_page.validation_page(), "Login failed for valid credentials!"
                logger.info("Validation passed for success case")
            else:
                error_message = login_page.check_error_login_incorrect()
                assert error_message in status, f"Expected: {status}, Got: {error_message}"
                logger.info("Validation passed for failure case")
