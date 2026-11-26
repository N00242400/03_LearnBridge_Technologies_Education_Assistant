# CA2 Student Starter Kit — Evidence-Based LangChain Agent

This folder is your Python + Gradio starting point for **CA2: AI Engineering — Evidence-Based LangChain Agent**.

> **Important:** Select **one** of the four open student case studies (`01_Helpwise_AI_Customer_Support`, `02_PeopleFirst_Systems_HR_Assistant`, `03_LearnBridge_Technologies_Education_Assistant`, or `04_DocuTech_AI_Technical_Documentation_Assistant`). Do **not** use `05_TripWise_In_Class_Example` for your submission.

---

## 1. Quick Start

```bash
# 1. Install dependencies into your virtual environment
pip install -r requirements.txt

# 2. Copy .env.example to .env and add your OPENROUTER_API_KEY
cp .env.example .env

# 3. Launch the Core Gradio UI
python app.py
```

---

## 2. What Is Included vs. What You Build

- **`app.py` (Full Core Level 1 Frontend Included):**
  Already renders all **Core (Level 1)** features out of the box:
  - Isolated multi-session switcher (`Session A` / `Session B` + `+ New Isolated Session`)
  - Chat interface calling `backend_contract.ask_agent(message, session_id)`
  - Core grounding `status` and `requires_human_review` escalation display
  - Core `evidence` citations (`doc_id`, `page`, `version`, `published_date`, `claim`, `quote`)
  - Core `uncertainties` bullet list and collapsible Raw JSON viewer
- **`backend_contract.py` (Connect Your Agent Here):**
  Replace the placeholder stub inside `ask_agent(message: str, session_id: str) -> dict` with your LangChain RAG agent and validated Pydantic `.model_dump()` output.
- **Level 2 & Architectural Extension UI (You Design & Extend):**
  `app.py` deliberately includes **only Core features**. As you engineer your Level 2 upgrades (advanced retrieval, quote/citation verification, indirect prompt-injection defences, token/cost telemetry) and your chosen Architectural Extension, use AI coding tools to extend `app.py` to display those new capabilities — and record how you verified the changes in your `ENGINEERING_REPORT.md` **AI Usage Log**.
- **`.env.example`:** Template environment file with zero secrets. Never commit your real `.env` file to Git!
