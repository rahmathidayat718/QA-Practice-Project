from venv import logger
from base.base_driver import BaseDriver
from pages.locator import Locator_Login as Lc
from utilities.custom_logger import Log_Maker


class LoginEcommercePage(BaseDriver):

    logger = Log_Maker.log_gen()

    def enter_email(self, email):
        if email is None:
            email = ""
        self.enter_text(Lc.email_id, email)
        logger.info("Entered Email : " + email)

    def enter_password(self, password):
        if password is None:
            password = ""
        self.enter_text(Lc.password_id, password)
        logger.info("Entered Password : " + password)

    def click_btn_submit(self):
        self.click(Lc.btn_submit_xpath)
        logger.info("Clicked Submit")

    def validation_page(self):
        try:
            self.find_element(Lc.ecommerce_title)
            return True
        except Exception as e:
            print("Login success :", e)
            return False

    def check_error_login_incorrect(self):
        error_element = self.find_element(Lc.error_incorrect)
        return error_element.text

    def check_error_login_empty_password(self):
        error_element = self.find_element(Lc.error_empty_password)
        return error_element.text

    def check_error_login_empty_username(self):
        error_element = self.find_element(Lc.error_empty_username)
        return error_element.text

    # test page
    def login_ecommerce(self, email, password):
        logger.info("Start Test")
        self.enter_email(email)
        self.enter_password(password)
        self.click_btn_submit()
        logger.info("End Test")