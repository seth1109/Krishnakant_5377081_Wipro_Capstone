import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            30
        )

    def open_first_product(self):

        # Wait for products
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.TAG_NAME,
                    "a"
                )
            )
        )

        time.sleep(5)

        # Find product links
        products = self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'product')]"
        )

        product_opened = False

        for product in products:

            try:

                href = product.get_attribute(
                    "href"
                )

                if href:

                    print(
                        f"Opening product: {href}"
                    )

                    # Open product in same tab
                    self.driver.get(href)

                    product_opened = True

                    break

            except Exception:
                continue

        if not product_opened:

            raise Exception(
                "Unable to open first product"
            )

        time.sleep(5)

    def add_product_to_cart(self):

        # Wait page load
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.TAG_NAME,
                    "body"
                )
            )
        )

        time.sleep(8)

        # Scroll page
        self.driver.execute_script(
            "window.scrollTo(0, 1000)"
        )

        time.sleep(5)

        # Close popup if exists
        try:

            popup_close = self.driver.find_element(
                By.XPATH,
                "//button[contains(@class,'close')]"
            )

            popup_close.click()

            print("Popup closed")

            time.sleep(2)

        except Exception:
            pass

        # Add to Bag locators
        possible_xpaths = [

            "//button[contains(.,'Add to Bag')]",

            "//span[contains(text(),'Add to Bag')]",

            "//button[@type='button']//span[contains(text(),'Add to Bag')]",

            "//button[contains(@class,'css')]",

            "//*[contains(text(),'Add to Bag')]",

            "//button[contains(.,'Add to Cart')]",

            "//*[contains(text(),'Add to Cart')]"

        ]

        button_found = False

        for xpath in possible_xpaths:

            try:

                elements = self.driver.find_elements(
                    By.XPATH,
                    xpath
                )

                for element in elements:

                    try:

                        if element.is_displayed():

                            self.driver.execute_script(
                                "arguments[0].scrollIntoView({block:'center'});",
                                element
                            )

                            time.sleep(2)

                            try:

                                element.click()

                            except Exception:

                                self.driver.execute_script(
                                    "arguments[0].click();",
                                    element
                                )

                            print(
                                "Add to Bag clicked"
                            )

                            button_found = True

                            break

                    except Exception:
                        continue

                if button_found:
                    break

            except Exception:
                continue

        if not button_found:

            self.driver.save_screenshot(
                "add_to_bag_error.png"
            )

            raise Exception(
                "Add to Bag button not found"
            )

        time.sleep(5)

    def open_cart(self):

        print("Opening cart directly")

        # Open cart directly
        self.driver.get(
            "https://www.nykaa.com/cart"
        )

        time.sleep(8)

        # Verify cart page loaded
        current_url = self.driver.current_url

        if "cart" not in current_url:

            raise Exception(
                "Unable to open cart"
            )

        print(
            "Cart opened successfully"
        )