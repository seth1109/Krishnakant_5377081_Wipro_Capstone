import csv


def get_products():

    products = []

    with open(
        "testdata/products.csv",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            products.append(row["product"])

    return products


EXPECTED_TITLE = "Nykaa"