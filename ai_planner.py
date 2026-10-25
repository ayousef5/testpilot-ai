# This file sends the user's testing instruction to OpenAI
# and asks the model to turn it into a structured test plan.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def create_test_plan(instruction):
    # Read the key from .env locally, or Streamlit Secrets online.
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        import streamlit as st
        api_key = st.secrets["OPENAI_API_KEY"]

    # Connect to OpenAI using the available API key.
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=(
            "You are a website testing planner. "
            "Create a short, clear test plan from the user's request. "
            "Do not execute actions or claim that a test passed. "
            "Return only the proposed steps and expected result."
        ),
        input=instruction,
    )

    return response.output_text


if __name__ == "__main__":
    plan = create_test_plan(
        "Test login with an incorrect password on SauceDemo."
    )
    print(plan)
