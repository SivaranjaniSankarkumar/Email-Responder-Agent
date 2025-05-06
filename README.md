# Automated Email Responder Agent

This project is an **Automated Email Responder Agent** that classifies incoming emails, generates smart professional replies, and refines them based on user feedback — powered by **Groq’s LLaMA3-70B** model and deployed using **Streamlit Cloud**.

---

##  Features

- **Email Classification**: Automatically detects the type of email (e.g., complaint, meeting, follow-up).
- **Smart Reply Generation**: Generates a professional and polite response tailored to the category.
- **Refinement via Feedback**: Accepts user feedback to improve the tone or content of the reply.
- **Interactive Web UI**: Clean, minimal Streamlit interface for easy use.

---

## 🚀 Demo

Live App: [Try it on Streamlit](https://email-responder-agent-j9un5dmuya5gdr9rskkpbr.streamlit.app/)
Walkthrough Video: (https://vimeo.com/1081871584/84b1f073a4)





---

## Tech Stack

- **Language Model**: `llama3-70b-8192` from Groq (OpenAI-compatible)
- **Frontend**: Streamlit
- **Backend API**: Groq’s OpenAI-compatible API
- **Deployment**: Streamlit Cloud

---

## How It Works

1. User pastes email content.
2. The app sends the content to Groq LLM for classification.
3. Based on category, the assistant generates a smart reply.
4. If feedback is provided, a refined version of the reply is generated.

---


