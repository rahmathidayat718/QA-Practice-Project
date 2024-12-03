import time
from pages.ecommerce.login_ecommerce_page import LoginEcommercePage


class TestLoginEcommerce:

    def test_ecommerce_login(self, driver, config_data, data_login_ecommerce):
        login_page = LoginEcommercePage
        driver.get(config_data["login_url_page"])

        email, password, exp_result = data_login_ecommerce
        login_page.login(email, password, exp_result)

        # Validate login
        if exp_result == "empty email":
            assert login_page.check_error_login_empty_username == "Bad credentials! Please try again! Make sure that you've registered."
        elif exp_result == "empty password":
            assert login_page.check_error_login_empty_password == "Bad credentials! Please try again! Make sure that you've registered."
        elif exp_result == "empty email and password":
            assert login_page.check_error_login_empty_username == "Bad credentials! Please try again! Make sure that you've registered."
            assert login_page.check_error_login_empty_password == "Bad credentials! Please try again! Make sure that you've registered."
        elif exp_result == "error":
            assert login_page.check_error_login_incorrect == "Bad credentials! Please try again! Make sure that you've registered."
        elif exp_result == "success":
            assert login_page.validation_page
            time.sleep(1)
