from venv import logger

from base.base_driver import BaseDriver
from utilities.custom_logger import Log_Maker
from pages.locator import LocatorAddToCart as Lc


class AddToCart(BaseDriver):

    logger = Log_Maker.log_gen()

    # scroll berdasarkan element tertentu
    def scroll_to_item(self):
        self.scroll_to_element(Lc.handphone_element)
        logger.info("Scroll Ke Element yang di tentukan")

    # add to cart
    def add_to_cart(self):
        self.click(Lc.add_handphone1)
        logger.info("Menambahkan Handphone ke Cart")
        self.click(Lc.add_handphone2)
        logger.info("Menambahkan Handphone ke Cart")

    # Scroll
    def scroll_to_top_page(self):
        self.scroll_to_top()
        logger.info("Scroll Ke Halaman Paling Atas")

    def test_add_to_cart(self):
        self.scroll_to_item()
        self.add_to_cart()
        self.scroll_to_top_page()

    #validation
    def validation(self):
        exp1 = self.find_element(Lc.validasi_hp1).text
        exp2 = self.find_element(Lc.validasi_hp2).text
        # Memeriksa apakah item yang diharapkan ada dalam validasi
        if exp1 == "Apple iPhone 13, 128GB, Blue" and exp2 == "Nokia 105, Black":
            logger.info("Both items successfully added to cart")
        elif exp1 == "Apple iPhone 13, 128GB, Blue" or exp2 == "Nokia 105, Black":
            logger.info("One of the items was successfully added to cart")
        else:
            logger.info(f"Items not added to cart. Expected: 'Apple iPhone 13, 128GB, Blue' or 'Nokia 105, Black', but got '{exp1}' and '{exp2}'")