
# TestPilot AI

An AI-assisted website testing demo built with Python, Streamlit,
OpenAI, and Playwright.

## Features

- Generates test plans from natural-language instructions
- Automates an invalid-login test using Playwright
- Verifies the actual error message
- Displays a screenshot of the browser result

## Current limitation

The initial demo supports the SauceDemo invalid-login scenario.
The AI generates the plan, while the implemented Playwright
test executes a predefined scenario.

## Run locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

   pip install -r requirements.txt
   playwright install chromium

3. Create a `.env` file with your OpenAI API key:

   OPENAI_API_KEY=your_api_key_here

4. Run:

   streamlit run app.py
