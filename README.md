# Non-Agentic Practice Resume Screening

A non-agentic practice application that automates resume screening using the Gemini 2.5 Flash model via the Google GenAI SDK. It compares an uploaded PDF resume against a provided job description, offering a match percentage, status recommendation, and concise feedback.

## 🚀 Project Architecture

```text
├── Backend
│   ├── app.py            # FastAPI main entry point
│   ├── schemas.py        # Pydantic data schemas
│   └── routes
│       └── screening.py  # GenAI client logic & API endpoint
└── Frontend
    └── app.py            # Streamlit UI
