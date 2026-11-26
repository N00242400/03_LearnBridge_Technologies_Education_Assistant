"""
CA2 Starter Backend Contract
============================
Replace the stub inside `ask_agent()` with your own LangChain RAG agent.

1. Core (Level 1): Return the 6 Core fields below (`answer`, `status`, `evidence`,
   `uncertainties`, `requires_human_review`, `escalation_reason`) from your validated
   Pydantic schema (`.model_dump()`). `app.py` already renders all Core fields!
2. Level 2 & Extensions: When you build your reliability, security, telemetry, and
   architectural extension features, you may include extra keys in this dictionary
   and extend `app.py` to display them cleanly.
"""


def ask_agent(message: str, session_id: str) -> dict:
    """
    Send one user message to your policy assistant for a specific `session_id`.

    Args:
        message: The user's question or follow-up message.
        session_id: Unique conversation ID (keeps Session A isolated from Session B).

    Returns:
        Dictionary matching your validated Pydantic response schema.
    """
    # TODO: Replace this placeholder dictionary with your LangChain agent call!
    return {
        "answer": (
            f"[Starter Stub — `{session_id}`] You asked: '{message}'. "
            "Connect your LangChain RAG agent inside `backend_contract.py`!"
        ),
        "status": "abstained",  # supported | partial | abstained | conflict_detected | escalated
        "evidence": [
            {
                "claim": "Sample placeholder citation (replace with real retrieved PDF evidence).",
                "doc_id": "SAMPLE-DOC-01",
                "version": "1.0",
                "published_date": "2026-02-15",
                "page": 1,
                "quote": "Replace this stub in backend_contract.py with your validated Pydantic output.",
            }
        ],
        "uncertainties": [
            "Backend RAG pipeline is not connected yet (currently returning starter stub)."
        ],
        "requires_human_review": False,
        "escalation_reason": "",
    }
