import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.homepage import HomePage
from pages.searchpage import SearchPage
from pages.cartpage import CartPage

from utils.config_reader import ConfigReader
from utils.logger import get_logger


logger = get_logger()


@pytest.mark.parametrize(
    "product",
    [
        "Vitamin"
    ]
)

def test_end_to_end_flow(driver, product):

    logger.info(
        f"E2E flow started for {product}"
    )

    wait = WebDriverWait(driver, 30)

    config = ConfigReader()

    home = HomePage(driver)

    search = SearchPage(driver)

    cart = CartPage(driver)

    try:

        # Open Homepage
        home.open_homepage(
            config.get_base_url()
        )

        logger.info(
            "Homepage opened successfully"
        )

        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        # Open Health & Wellness
        home.open_health_and_wellness()

        logger.info(
            "Health & Wellness section opened"
        )

        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        # Search Product
        search.search_product(product)

        logger.info(
            f"{product} searched successfully"
        )

        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        # Open First Product
        cart.open_first_product()

        logger.info(
            "First product opened successfully"
        )

        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        # Scroll Page
        driver.execute_script(
            "window.scrollTo(0, 500)"
        )

        # Add Product To Cart
        cart.add_product_to_cart()

        logger.info(
            f"{product} added to cart successfully"
        )

        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        # Open Bag
        cart.open_cart()

        logger.info(
            "Bag opened successfully"
        )

        print(
            f"{product} E2E flow executed successfully"
        )

    except Exception as e:

        logger.error(
            f"{product} E2E flow failed: {e}"
        )

        driver.save_screenshot(
            f"{product}_failure.png"
        )

        print(
            f"Test failed for {product}"
        )

        raise