from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    def scroll_by_pixel(self, x=0, y=500):
        """Scroll by pixel (default is 500px down)."""
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_element(self, element):
        """Scroll to a specific element."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_with_action_chains(self, x=0, y=500):
        """Scroll using ActionChains."""
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(x, y).perform()
