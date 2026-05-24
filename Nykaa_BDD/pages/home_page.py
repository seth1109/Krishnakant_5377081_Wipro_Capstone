from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time


class HomePage(BasePage):

    SEARCH_BOX = (
        By.NAME,
        "search-suggestions-nykaa"
    )

    def search_product(self, product):

        self.enter_text(self.SEARCH_BOX, product)

        search = self.driver.find_element(*self.SEARCH_BOX)

        search.send_keys(Keys.ENTER)

        time.sleep(5)