Feature: Nykaa Positive Test Cases

    Scenario: Validate Nykaa Website Title

        Given User launches Nykaa website
        Then Title should contain "Nykaa"


    Scenario: Search Protein Product

        Given User launches Nykaa website
        When User searches for "Protein"
        Then Search results should be displayed


    Scenario: Search Vitamin Product

        Given User launches Nykaa website
        When User searches for "Vitamin C"
        Then Search results should be displayed


    Scenario: Search Hair Care Product

        Given User launches Nykaa website
        When User searches for "Shampoo"
        Then Search results should be displayed


    Scenario: Search Skin Care Product

        Given User launches Nykaa website
        When User searches for "Face Wash"
        Then Search results should be displayed