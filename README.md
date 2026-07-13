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

```

---

## 🛠️ Features

* **FastAPI Backend:** Handles incoming files, connects to the Gemini API, and enforces strict JSON responses.
* **Streamlit Frontend:** Clean user interface to paste job requirements and upload PDF resumes.
* **Structured Outputs:** Uses Pydantic schemas via Gemini's `response_schema` configuration to ensure reliable status tracking and scoring without fragile prompt parsing.

---

## ⚙️ Setup and Installation

### Prerequisites

* Python 3.10+
* A Gemini API Key from Google AI Studio.

### 1. Backend Setup

1. Navigate to the backend directory:
```bash
cd Backend

```


2. Install dependencies:
```bash
pip install fastapi google-genai python-dotenv pydantic

```


3. Create a `.env` file in the `Backend/` directory:
```env
GEMINI_RESUME_SCREENING_API=your_actual_gemini_api_key_here

```


4. Start the backend server:
```bash
fastapi dev app.py

```


The backend will run at `http://localhost:8000`.

### 2. Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd Frontend

```


2. Install dependencies:
```bash
pip install streamlit requests

```


3. Run the Streamlit application:
```bash
streamlit run app.py

```


The frontend UI will open automatically in your web browser.

---

## 💡 Tech Stack

* **Frontend:** Streamlit, Requests
* **Backend:** FastAPI, Pydantic
* **LLM Integration:** Google GenAI SDK (`gemini-2.5-flash`)

```

```
