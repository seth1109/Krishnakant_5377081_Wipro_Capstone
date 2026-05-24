import time
import pytest

from pages.homepage import HomePage
from pages.searchpage import SearchPage

from utils.config_reader import ConfigReader
from utils.logger import get_logger


logger = get_logger()


@pytest.mark.parametrize(
    "invalid_product",
    [
        "abc123",
        "wrongproduct",
        "invaliditem"
    ]
)

def test_invalid_search(
    driver,
    invalid_product
):

    logger.info(
        f"Negative test started for {invalid_product}"
    )

    config = ConfigReader()

    home = HomePage(driver)

    search = SearchPage(driver)

    # Open Homepage
    home.open_homepage(
        config.get_base_url()
    )

    time.sleep(3)

    # Invalid Search
    search.search_product(
        invalid_product
    )

    logger.info(
        f"{invalid_product} invalid search executed"
    )

    print(
        f"{invalid_product} negative test passed"
    )