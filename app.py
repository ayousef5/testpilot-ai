import streamlit as st

from ai_planner import create_test_plan
from browser_tester import run_login_test

# Set up the web page.
st.set_page_config(page_title="TestPilot AI", page_icon="🧪")
st.title("🧪 TestPilot AI")
st.write("AI-powered website testing using OpenAI and Playwright.")

# Let the user describe what they want to test.
instruction = st.text_area(
    "Testing instruction",
    value="Test login with an incorrect password on SauceDemo.",
)

# Run the test when the user clicks the button.
if st.button("Run AI Test", type="primary"):
    # Only execute the scenario we have implemented so far.
    supported = (
        "login" in instruction.lower()
        and any(
            word in instruction.lower()
            for word in ["incorrect password", "wrong password", "invalid password"]
        )
    )

    if not supported:
        st.warning(
            "Currently, this demo supports testing login "
            "with an incorrect password. Try that instruction."
        )
    else:
        try:
            # Ask the AI to generate a plan.
            with st.spinner("AI is creating a test plan..."):
                plan = create_test_plan(instruction)

            st.subheader("AI-generated test plan")
            st.write(plan)

            # Execute the browser test.
            with st.spinner("Playwright is testing the website..."):
                result = run_login_test()

            # Display the actual browser test result.
            st.subheader("Test results")

            if result["passed"]:
                st.success("PASS: The expected error message appeared.")
            else:
                st.error("FAIL: The expected error message did not match.")

            st.write("Observed message:", result["error_message"])

            # Display the screenshot captured by Playwright.
            st.subheader("Browser screenshot")
            st.image(result["screenshot"])

        except Exception as error:
            st.error(f"The test could not complete: {error}")
