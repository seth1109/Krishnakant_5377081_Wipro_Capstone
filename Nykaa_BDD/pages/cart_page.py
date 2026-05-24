from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class CartPage(BasePage):

    def open_cart(self):

        cart_xpaths = [
            '//*[contains(text(),"Bag")]',
            '//button[contains(@class,"cart")]'
        ]

        for xpath in cart_xpaths:

            try:

                self.click((By.XPATH, xpath))

                break

            except:
                continue

        time.sleep(5)

    def verify_product(self):

        body = self.driver.find_element(
            By.TAG_NAME,
            "body"
        ).text.lower()

        keywords = [
            "optimum",
            "whey",
            "protein"
        ]

        for word in keywords:

            if word in body:
                return True

        return False