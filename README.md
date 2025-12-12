# Car Routes Lab

## Overview
This lab introduces basic Flask routing concepts using a minimal web application.  
The focus is on defining static and dynamic routes and validating behavior using pytest.

---

## Project Structure

car-routes-lab/

car-routes-lab/server/

car-routes-lab/server/app.py

car-routes-lab/server/testing/

car-routes-lab/server/testing/app_test.py

car-routes-lab/server/testing/conftest.py

car-routes-lab/pytest.ini

car-routes-lab/README.md

- server/app.py contains the Flask application and route definitions
- server/testing/app_test.py holds automated tests for each route
- pytest.ini configures pytest to correctly locate application modules

## Application Overview
The Flask app provides two routes:

/
- Displays a welcome message for Flatiron Cars.

/<model>
- Accepts a dynamic URL segment representing a car model.
- If the model exists in the predefined catalog, a success message is returned.
- Otherwise, an error message is displayed.

- All responses are returned as plain text to simplify testing and validation.

## Key Features
- Basic Flask application setup
- Static and dynamic route handling
- Simple in-memory data validation
- Automated testing using Flask’s test client and pytest

## Running the Tests

From the project root use the following:
- python -m pytest

## General project notes

Project passed through ChatGPT to find syntax errors, spelling and grammar errors, and to write a quick overview README.md file. README.md was reviewed and edited for clarity and readability prior to submission.