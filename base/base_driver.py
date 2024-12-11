from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BaseDriver:

    driver: WebDriver

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        try:
            # Menunggu hingga elemen tersedia dan dapat di-interaksi (klik)
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"Elemen dengan locator {locator} tidak ditemukan dalam {timeout} detik.")
            return None
    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def enter_text(self, locator, text, timeout=10):
        try:
            # Menunggu elemen tersedia
            element = self.find_element(locator, timeout)
            if element:
                element.clear()  # Menghapus teks yang sudah ada sebelumnya (opsional)
                element.send_keys(text)  # Memasukkan teks
                return element
            else:
                print(f"Elemen dengan locator {locator} tidak ditemukan untuk memasukkan teks.")
                return None
        except Exception as e:
            print(f"Terjadi kesalahan saat mencoba memasukkan teks ke elemen: {e}")
            return None
    def click(self, locator):
        self.find_element(locator).click()


    # Scroll
    def scroll_to_element(self, locator):
        """Scroll ke elemen tertentu menggunakan ActionChains"""
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to_bottom(self):
        """Scroll ke bagian bawah halaman menggunakan JavaScript"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_by_offset(self, x=0, y=500):
        """Scroll halaman secara manual dengan offset"""
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_top(self):
        """Scroll ke atas halaman (paling atas)"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    # Metode untuk memilih opsi dalam dropdown berdasarkan teks
    def select_dropdown_by_visible_text(self, locator, text, timeout=10):
        try:
            dropdown_element = self.find_element(locator, timeout)
            if dropdown_element:
                select = Select(dropdown_element)
                select.select_by_visible_text(text)
                return True
            else:
                print(f"Dropdown dengan locator {locator} tidak ditemukan untuk memilih berdasarkan teks.")
                return False
        except Exception as e:
            print(f"Terjadi kesalahan saat memilih dropdown berdasarkan teks: {e}")
            return False

    # Metode untuk memilih opsi dalam dropdown berdasarkan nilai (value)
    def select_dropdown_by_value(self, locator, value, timeout=10):
        try:
            dropdown_element = self.find_element(locator, timeout)
            if dropdown_element:
                select = Select(dropdown_element)
                select.select_by_value(value)
                return True
            else:
                print(f"Dropdown dengan locator {locator} tidak ditemukan untuk memilih berdasarkan nilai.")
                return False
        except Exception as e:
            print(f"Terjadi kesalahan saat memilih dropdown berdasarkan nilai: {e}")
            return False

    # Metode untuk memilih opsi dalam dropdown berdasarkan indeks
    def select_dropdown_by_index(self, locator, index, timeout=10):
        try:
            dropdown_element = self.find_element(locator, timeout)
            if dropdown_element:
                select = Select(dropdown_element)
                select.select_by_index(index)
                return True
            else:
                print(f"Dropdown dengan locator {locator} tidak ditemukan untuk memilih berdasarkan indeks.")
                return False
        except Exception as e:
            print(f"Terjadi kesalahan saat memilih dropdown berdasarkan indeks: {e}")
            return False

    # Metode untuk mendapatkan semua opsi dalam dropdown
    def get_all_dropdown_options(self, locator, timeout=10):
        try:
            dropdown_element = self.find_element(locator, timeout)
            if dropdown_element:
                select = Select(dropdown_element)
                return [option.text for option in select.options]
            else:
                print(f"Dropdown dengan locator {locator} tidak ditemukan untuk mendapatkan semua opsi.")
                return []
        except Exception as e:
            print(f"Terjadi kesalahan saat mendapatkan semua opsi dalam dropdown: {e}")
            return []
