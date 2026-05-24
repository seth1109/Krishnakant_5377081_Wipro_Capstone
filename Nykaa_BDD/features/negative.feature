Feature: Nykaa Negative Test Cases

    Scenario: Search Invalid Product

        Given User launches Nykaa website
        When User searches for "invalidproduct123"
        Then No product message should be displayed

    Scenario: Add unavailable product to cart

        Given User launches Nykaa website
        When User searches for "invalidvitamin999"
        Then Add to Bag button should not be visible