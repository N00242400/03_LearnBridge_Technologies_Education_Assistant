"""
CA2 Student Starter Kit — Core (Level 1) Gradio Frontend
========================================================
Run with:
    python app.py

What is ALREADY included out of the box (Core Level 1 Features):
  - Isolated multi-session selector (`Session A` / `Session B` + `+ New Isolated Session`)
  - Chat conversation view connected to `backend_contract.ask_agent(message, session_id)`
  - Core grounding `status` and `requires_human_review` escalation display
  - Core `evidence` citations list (`doc_id`, `page`, `version`, `published_date`, `claim`, `quote`)
  - Core `uncertainties` bullet list and collapsible Raw JSON viewer

What YOU will extend in Level 2 & Your Architectural Extension:
  - As you add Level 2 reliability, security, telemetry, and your chosen extension in
    your backend, use AI coding tools to extend this UI to surface those new features
    (e.g., quote-verification status, source trust/security warnings, retrieved-chunk
    inspection, token/cost telemetry) — and document your verification in your AI Usage Log!
"""

import json
import uuid
import gradio as gr
from dotenv import load_dotenv

from backend_contract import ask_agent

load_dotenv(override=True)


def init_sessions() -> dict:
    return {
        "Session A": {"id": f"session-a-{uuid.uuid4().hex[:6]}", "history": []},
        "Session B": {"id": f"session-b-{uuid.uuid4().hex[:6]}", "history": []},
    }


def format_status(resp: dict) -> str:
    status = resp.get("status", "abstained").upper()
    lines = [f"**Status:** `{status}`"]
    if resp.get("requires_human_review"):
        reason = resp.get("escalation_reason") or "Specialist human review required."
        lines.append(f"\n> **Human Review Required:** {reason}")
    return "\n".join(lines)


def format_citations(evidence: list[dict]) -> str:
    if not evidence:
        return "*No supporting citations returned for this turn.*"
    blocks = []
    for i, ev in enumerate(evidence, start=1):
        meta = f"Page {ev.get('page', '?')}"
        if ev.get("version"):
            meta += f", v{ev['version']}"
        if ev.get("published_date"):
            meta += f", {ev['published_date']}"
        blocks.append(
            f"**{i}. `{ev.get('doc_id', '?')}`** ({meta})\n"
            f"- **Claim:** {ev.get('claim', '')}\n"
            f"- **Quote:** *\"{ev.get('quote', '')}\"*"
        )
    return "\n\n".join(blocks)


def format_uncertainties(items: list[str]) -> str:
    return "\n".join(f"- {u}" for u in items) if items else "*None*"


def handle_message(user_message: str, label: str, sessions: dict):
    sess = sessions[label]
    if not user_message.strip():
        return "", sess["history"], sessions, "*Ready*", "*None*", "*None*", "{}"

    resp = ask_agent(message=user_message, session_id=sess["id"])
    sess["history"] = sess["history"] + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": resp["answer"]},
    ]
    return (
        "",
        sess["history"],
        sessions,
        format_status(resp),
        format_citations(resp.get("evidence", [])),
        format_uncertainties(resp.get("uncertainties", [])),
        json.dumps(resp, indent=2),
    )


def switch_session(label: str, sessions: dict):
    sess = sessions[label]
    return sess["history"], f"Active `session_id`: `{sess['id']}`", "*Switched session*", "*None*", "*None*", "{}"


def create_new_session(sessions: dict):
    label = f"Session {len(sessions) + 1}"
    sid = f"session-{uuid.uuid4().hex[:6]}"
    sessions[label] = {"id": sid, "history": []}
    return gr.update(choices=list(sessions.keys()), value=label), sessions, [], f"Active `session_id`: `{sid}`", "*New isolated session*", "*None*", "*None*", "{}"


with gr.Blocks(title="CA2 Evidence-Based Policy Assistant") as demo:
    sessions_state = gr.State(init_sessions)

    gr.Markdown("## CA2 Evidence-Based Policy Assistant *(Core Starter Frontend)*")
    with gr.Row():
        session_dd = gr.Dropdown(label="Session (Isolated Memory)", choices=["Session A", "Session B"], value="Session A", scale=3)
        new_session_btn = gr.Button("+ New Isolated Session", scale=1)
        session_label = gr.Markdown("Active `session_id`: *(initialising)*")

    with gr.Row():
        with gr.Column(scale=6):
            chatbot = gr.Chatbot(label="Conversation", height=380)
            msg_box = gr.Textbox(
                label="Ask a policy or technical documentation question",
                placeholder="Type your question and press Enter...",
            )
            send_btn = gr.Button("Send", variant="primary")

        with gr.Column(scale=5):
            gr.Markdown("### Grounding Status & Escalation")
            status_md = gr.Markdown("*Send a message to view grounding status.*")
            gr.Markdown("### Supporting Citations")
            citations_md = gr.Markdown("*None*")
            gr.Markdown("### Uncertainties & Missing Details")
            uncertainties_md = gr.Markdown("*None*")
            with gr.Accordion("Raw Structured Response JSON", open=False):
                raw_json = gr.Code(language="json", value="{}")

    demo.load(fn=lambda s: f"Active `session_id`: `{s['Session A']['id']}`", inputs=[sessions_state], outputs=[session_label])
    outputs = [msg_box, chatbot, sessions_state, status_md, citations_md, uncertainties_md, raw_json]
    msg_box.submit(handle_message, inputs=[msg_box, session_dd, sessions_state], outputs=outputs)
    send_btn.click(handle_message, inputs=[msg_box, session_dd, sessions_state], outputs=outputs)
    session_dd.change(switch_session, inputs=[session_dd, sessions_state], outputs=[chatbot, session_label, status_md, citations_md, uncertainties_md, raw_json])
    new_session_btn.click(create_new_session, inputs=[sessions_state], outputs=[session_dd, sessions_state, chatbot, session_label, status_md, citations_md, uncertainties_md, raw_json])


if __name__ == "__main__":
    demo.launch()
