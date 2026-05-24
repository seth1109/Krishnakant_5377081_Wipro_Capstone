from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ProductPage(BasePage):

    FIRST_PRODUCT = (
        By.XPATH,
        '(//a[contains(@href,"/p/")])[1]'
    )

    ADD_TO_BAG = (
        By.XPATH,
        '//button[contains(.,"Add to Bag")]'
    )

    def open_product(self):

        product = self.wait.until(
            lambda d: d.find_element(*self.FIRST_PRODUCT)
        )

        product_url = product.get_attribute("href")

        self.driver.get(product_url)

        time.sleep(5)

    def add_to_cart(self):

        self.click(self.ADD_TO_BAG)

        time.sleep(5)