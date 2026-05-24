import time

from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):

    SIGNIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Sign in')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@type='tel']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def open_login_popup(self):

        time.sleep(3)

        self.click(
            self.SIGNIN_BUTTON
        )

    def enter_mobile_number(self, mobile):

        time.sleep(2)

        self.enter_text(
            self.MOBILE_INPUT,
            mobile
        )

    def click_continue(self):

        time.sleep(2)

        self.click(
            self.CONTINUE_BUTTON
        )