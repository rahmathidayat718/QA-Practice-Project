from base.base_driver import BaseDriver
from utilities.custom_logger import Log_Maker
from pages.locator import LocatorAddToCart as Lc


class AddToCart(BaseDriver):

    logger = Log_Maker.log_gen()

    # scroll
    def scroll_to_item(self):
        self.scroll_to_element(Lc.handphone_element)