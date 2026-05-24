# Nykaa Health & Wellness Automation Framework

## Project Description

This project is developed using Selenium with Python BDD framework for automating Nykaa Health & Wellness website.

The framework covers:
- Positive Test Cases
- Negative Test Cases
- End To End Testing
- Allure Reporting
- Screenshot Capture

---

## Technologies Used

- Python
- Selenium WebDriver
- Behave (BDD Framework)
- Allure Reports
- ChromeDriver

---

## Project Structure

Krishnakant_5377081_Wipro_BDD_Capstone/

│

├── features/

│   ├── positive.feature

│   ├── negative.feature

│   ├── nykaa_e2e.feature

│   ├── environment.py

│   │

│   └── steps/

│       └── e2e_steps.py

│

├── screenshots/

├── allure-results/

└── README.md

---

## Features Covered

### Positive Test Cases
- Search Protein Product
- Search Vitamin Product
- Search Hair Care Product
- Validate Website Title
- Search Skin Care Product

### Negative Test Cases
- Invalid Product Search
- Product Without Add To Bag

### End To End Flow
- Search Product
- Open Product
- Add Product To Cart

---

## How To Run Tests

Run all test cases:

```powershell
behave