from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def click(self, locator):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    def get_title(self):

        return self.driver.title

    def press_enter(self, locator):

        self.driver.find_element(
            *locator
        ).send_keys(Keys.ENTER)

    def js_click(self, locator):

        element = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )