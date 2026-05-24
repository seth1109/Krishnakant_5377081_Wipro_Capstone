from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ====================== LAUNCH WEBSITE ====================== #

@given('User launches Nykaa website')
def launch_website(context):

    context.driver.get("https://www.nykaa.com/")

    context.driver.maximize_window()

    time.sleep(5)


# ====================== SEARCH PRODUCT ====================== #

@when('User searches for "{product}"')
def search_product(context, product):

    wait = WebDriverWait(context.driver, 50)

    search_box = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@placeholder='Search on Nykaa']")
        )
    )

    search_box.clear()

    time.sleep(2)

    search_box.send_keys(product)

    time.sleep(4)

    search_box.send_keys(Keys.ENTER)

    time.sleep(10)


# ====================== VERIFY SEARCH RESULTS ====================== #

@then('Search results should be displayed')
def verify_search_results(context):

    time.sleep(8)

    products = context.driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'/p/')]"
    )

    assert len(products) > 0, "Search results are not displayed"


# ====================== VALIDATE TITLE ====================== #

@then('Title should contain "{text}"')
def validate_title(context, text):

    actual_title = context.driver.title

    assert text.lower() in actual_title.lower()


# ====================== ADD PRODUCT TO CART ====================== #

@when('User adds product to cart')
def add_product_to_cart(context):

    wait = WebDriverWait(context.driver, 60)

    time.sleep(10)

    product_links = context.driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'/p/')]"
    )

    if len(product_links) == 0:

        raise Exception("No products found")

    first_product = product_links[0]

    context.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        first_product
    )

    time.sleep(3)

    context.driver.execute_script(
        "arguments[0].click();",
        first_product
    )

    time.sleep(8)

    tabs = context.driver.window_handles

    context.driver.switch_to.window(tabs[-1])

    time.sleep(10)

    buttons = context.driver.find_elements(
        By.TAG_NAME,
        "button"
    )

    add_to_bag = None

    for button in buttons:

        text = button.text.strip().lower()

        if (
            "add to bag" in text
            or "add to cart" in text
        ):

            add_to_bag = button
            break

    if add_to_bag is None:

        raise Exception("Add To Bag button not found")

    context.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        add_to_bag
    )

    time.sleep(3)

    context.driver.execute_script(
        "arguments[0].click();",
        add_to_bag
    )

    time.sleep(8)


# ====================== VERIFY PRODUCT ADDED ====================== #

@then('Product should be added successfully')
def verify_product_added(context):

    time.sleep(5)

    page_source = context.driver.page_source.lower()

    assert (
        "bag" in page_source
        or "added to bag" in page_source
        or "shopping bag" in page_source
    ), "Product not added successfully"


# ====================== NEGATIVE TESTCASE 1 ====================== #

@then('No product message should be displayed')
def no_product_found(context):

    time.sleep(5)

    page_source = context.driver.page_source.lower()

    assert (
        "no products found" in page_source
        or "0 result" in page_source
        or "sorry" in page_source
        or "couldn't find" in page_source
    ), "No product message not displayed"


# ====================== NEGATIVE TESTCASE 2 ====================== #

@then('Add to Bag button should not be visible')
def add_button_not_visible(context):

    time.sleep(5)

    buttons = context.driver.find_elements(
        By.XPATH,
        "//button[contains(.,'Add to Bag')]"
    )

    assert len(buttons) == 0, "Add To Bag button is visible"