# This file contains a Playwright-based test for logging into the SauceDemo website with an incorrect password.
from playwright.sync_api import sync_playwright


def run_login_test():
    # Start Playwright and launch a browser.
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)

        # Open a new browser page.
        page = browser.new_page()

        # Visit the demo website.
        page.goto("https://www.saucedemo.com/")

        # Enter a known username and an incorrect password.
        page.locator('[data-test="username"]').fill("standard_user")
        page.locator('[data-test="password"]').fill("wrong_password")

        # Click the login button.
        page.locator('[data-test="login-button"]').click()

        # Read the error message displayed by the website.
        error = page.locator('[data-test="error"]').inner_text()

        # Check whether the expected error appeared.
        expected_error = (
            "Epic sadface: Username and password do not match "
            "any user in this service."
        )
        passed = expected_error.rstrip(".") == error.rstrip(".")

        # Save a screenshot for our report.
        page.screenshot(path="test-result.png")

        # Close the browser when the test is finished.
        browser.close()

        # Return the real result to the caller.
        return {
            "passed": passed,
            "error_message": error,
            "screenshot": "test-result.png",
        }


# Run the test when this file is executed directly.
if __name__ == "__main__":
    result = run_login_test()
    print(result)
