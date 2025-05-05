code = """# app.py

import streamlit as st
import openai
import os

# Load API key from secrets or environment
try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found. Use secrets.toml (Streamlit Cloud) or %env (Colab).")
    st.stop()

# Initialize Groq LLaMA3 client
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama3-70b-8192"

# UI configuration
st.set_page_config(page_title="AI Email Assistant", layout="centered")
st.title("AI Email Assistant")
st.markdown("This tool classifies, responds to, and refines email content using the Groq LLaMA3-70B model.")

# Prompt templates
def build_classification_prompt(email: str) -> str:
    return f\"""You are an email classifier.
Classify the email into one of the following:
- meeting
- complaint
- follow-up
- general
- others

Email:
{email.strip()}

Category:\"""


def build_reply_prompt(email: str, category: str) -> str:
    return f\"""You are a helpful, polite, and professional email assistant.
Category: {category}

Email:
{email.strip()}

Generate a smart and professional reply:\"""


def build_refine_prompt(original: str, feedback: str) -> str:
    return f\"""You are a professional email assistant.
Refine the original reply based on the user feedback below.
Ensure the tone is respectful and clear.

Original Reply:
{original.strip()}

User Feedback:
{feedback.strip()}

Refined Reply:\"""


# LLM generator
def generate_completion(prompt: str, max_tokens: int = 200) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error("Groq API call failed.")
        print(e)
        return "Error: Unable to generate response."


# Agents
class EmailAgent:
    def classify_email(self, body: str) -> str:
        prompt = build_classification_prompt(body)
        return generate_completion(prompt, max_tokens=10).lower()

    def generate_reply(self, body: str, category: str) -> str:
        prompt = build_reply_prompt(body, category)
        return generate_completion(prompt)


class FeedbackHandler:
    def refine_reply(self, original: str, feedback: str) -> str:
        prompt = build_refine_prompt(original, feedback)
        return generate_completion(prompt)


# Initialize
agent = EmailAgent()
refiner = FeedbackHandler()

# Input
st.subheader("Email Input")
email_text = st.text_area("Paste the email body here", height=200)

if "reply" not in st.session_state:
    st.session_state.reply = ""
if "category" not in st.session_state:
    st.session_state.category = ""

# Generate
if st.button("Generate Reply"):
    if not email_text.strip():
        st.warning("Please enter an email.")
    else:
        with st.spinner("Processing..."):
            st.session_state.category = agent.classify_email(email_text)
            st.session_state.reply = agent.generate_reply(email_text, st.session_state.category)
        st.success(f"Category: {st.session_state.category.capitalize()}")

# Smart reply output
if st.session_state.reply:
    st.subheader("Smart Reply")
    st.text_area("Generated Reply", st.session_state.reply, height=150)

    st.subheader("Refine the Reply")
    feedback = st.text_input("Enter your feedback to improve the reply")

    if feedback and st.button("Refine Reply"):
        with st.spinner("Refining..."):
            refined = refiner.refine_reply(st.session_state.reply, feedback)
            st.subheader("Refined Reply")
            st.text_area("Refined Output", refined, height=150)
"""

# Save to app.py
with open("app.py", "w") as f:
    f.write(code)
