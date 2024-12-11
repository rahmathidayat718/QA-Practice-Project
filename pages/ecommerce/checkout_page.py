from venv import logger
from base.base_driver import BaseDriver
from utilities.custom_logger import Log_Maker
from pages.locator import LocatorAddToCart as Lc
from pages.locator import ShippingDetails as Lc
from utilities.excel_reader import ExcelReader


class CheckoutPage(BaseDriver):

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

    # validation
    def validation(self):
        exp1 = self.find_element(Lc.validasi_hp1).text
        exp2 = self.find_element(Lc.validasi_hp2).text
        # Memeriksa apakah item yang diharapkan ada dalam validasi
        if exp1 == "Apple iPhone 13, 128GB, Blue" and exp2 == "Nokia 105, Black":
            logger.info("Both items successfully added to cart")
        elif exp1 == "Apple iPhone 13, 128GB, Blue" or exp2 == "Nokia 105, Black":
            logger.info("One of the items was successfully added to cart")
        else:
            logger.info(
                f"Items not added to cart. Expected: 'Apple iPhone 13, 128GB, Blue' or 'Nokia 105, Black', but got '{exp1}' and '{exp2}'")

    def checkout_item(self):
        self.click(Lc.checkout)

    # submit_order
    def submit_order(self, phone_number, street, city, country):
        self.enter_text(Lc.phone_number, phone_number)
        logger.info("User memasukan phone number: " + str(phone_number))
        self.enter_text(Lc.street, street)
        logger.info("User memasukan Street: " + str(street))
        self.enter_text(Lc.city, city)
        logger.info("User memasukan city" + city)
        self.select_dropdown_by_visible_text(Lc.select_country, country)
        logger.info("User memilih county" + country)
        self.click(Lc.submit_order)
        logger.info("User Submit Order")

    def validation_submit(self):

        try:
            act_result = Lc.submit_validation.text
            excel_reader = ExcelReader("testdata/qa-practice-automation.xlsx")
            test_data = excel_reader.get_data(sheet_name="submit_order")
            expected_value = test_data['Congrats! Your order of '].value

            # Validasi
            if act_result == expected_value:
                logger.info("Validasi Berhasil: Data Sama")
                return True
            else:
                print("Validasi Gagal: Data Tidak Sama")
                return False

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            return False