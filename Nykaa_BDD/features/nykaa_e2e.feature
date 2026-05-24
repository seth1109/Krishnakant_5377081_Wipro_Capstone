Feature: Nykaa E2E Flow

    Scenario: Add Product To Cart

        Given User launches Nykaa website
        When User searches for "ON Whey Protein"
        And User adds product to cart
        Then Product should be added successfully