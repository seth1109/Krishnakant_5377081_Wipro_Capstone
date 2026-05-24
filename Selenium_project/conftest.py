import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    service = Service(
        r"C:\drivers\chromedriver-win64\chromedriver.exe"
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    driver.quit()