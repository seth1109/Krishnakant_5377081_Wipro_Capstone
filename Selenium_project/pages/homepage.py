from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class HomePage(BasePage):

    HOME_LOGO = (
        By.XPATH,
        "//img[@alt='Nykaa Fashion']"
    )

    HEALTH_WELLNESS = (
        By.XPATH,
        "//a[contains(text(),'Health & Wellness')]"
    )

    def open_homepage(self, url):

        self.driver.get(url)

    def verify_homepage(self):

        return self.driver.title

    def open_health_and_wellness(self):

        self.click(
            self.HEALTH_WELLNESS
        )