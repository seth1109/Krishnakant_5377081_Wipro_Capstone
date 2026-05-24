import os
import allure

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from allure_commons.types import AttachmentType


# ====================== BEFORE SCENARIO ====================== #

def before_scenario(context, scenario):

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    # ================= DRIVER PATH ================= #

    service = Service(
        r"C:\drivers\chromedriver-win64\chromedriver.exe"
    )

    # ================================================= #

    context.driver = webdriver.Chrome(
        service=service,
        options=options
    )


# ====================== AFTER EACH STEP ====================== #

def after_step(context, step):

    try:

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        safe_step_name = (
            step.name
            .replace(" ", "_")
            .replace('"', '')
            .replace("/", "_")
        )

        screenshot_path = (
            f"screenshots/{safe_step_name}_{timestamp}.png"
        )

        context.driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=step.name,
            attachment_type=AttachmentType.PNG
        )

    except Exception as e:

        print(f"Screenshot Error: {e}")


# ====================== AFTER SCENARIO ====================== #

def after_scenario(context, scenario):

    try:

        context.driver.quit()

    except:

        pass