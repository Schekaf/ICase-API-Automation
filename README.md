# Pytest API Framework for Petstore

This is a Python-based API testing framework using `pytest` to validate the functionality of the [Petstore API](https://petstore.swagger.io/). The framework is designed to facilitate CRUD (Create, Read, Update, Delete) operations on pet data.

## Features

- Perform CRUD operations on the Petstore API.
- Validate responses for different scenarios, including success and error cases.
- Use fixtures for consistent test data.
- Generate random numbers for dynamic test cases.

## Requirements

- Python 3.10 or higher
- `pytest` library
- `requests` library

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Schekaf/ICase-API-Automation.git
   
2. Install the required dependencies::
   ```bash
   pip install -r requirements.txt
   
3. Run Tests:
    ```bash
   pytest -v tests/test_pet_api.py
