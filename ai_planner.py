# This file sends the user's testing instruction to OpenAI
# and asks the model to turn it into a structured test plan.
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from our local .env file.
load_dotenv()

# Create a client that can send requests to OpenAI.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_test_plan(instruction):
    # Ask the AI to turn the user's instruction into a test plan.
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

    # Return the AI's text response to the caller.
    return response.output_text


# Run a quick test when this file is executed directly.
if __name__ == "__main__":
    plan = create_test_plan(
        "Test login with an incorrect password on SauceDemo."
    )
    print(plan)
