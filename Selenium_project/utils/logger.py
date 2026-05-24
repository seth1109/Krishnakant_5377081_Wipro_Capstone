import logging

logging.getLogger("WDM").setLevel(logging.ERROR)

def get_logger():

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        "logs/automation.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    return logger