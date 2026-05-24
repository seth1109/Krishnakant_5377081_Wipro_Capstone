import time
import pytest

from pages.homepage import HomePage
from pages.searchpage import SearchPage

from utils.config_reader import ConfigReader
from utils.logger import get_logger


logger = get_logger()


@pytest.mark.parametrize(
    "product",
    [
        "Vitamin",
        "Protein Powder",
        "Omega 3"
    ]
)

def test_search_products(
    driver,
    product
):

    logger.info(
        f"Positive test started for {product}"
    )

    config = ConfigReader()

    home = HomePage(driver)

    search = SearchPage(driver)

    # Open Homepage
    home.open_homepage(
        config.get_base_url()
    )

    time.sleep(3)

    # Search Product
    search.search_product(
        product
    )

    logger.info(
        f"{product} searched successfully"
    )

    print(
        f"{product} positive test passed"
    )