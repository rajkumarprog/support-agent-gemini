# Support Agent (Gemini CLI)

A command-line customer-support assistant written in Python. It reads a customer's question, detects what kind of user they are, finds the matching policy document, answers using Google Gemini, and decides whether the case should be handed off to a human agent.

## Features

- **Persona detection** – classifies the user as *Technical Expert*, *Frustrated User* or *Business Executive* and adjusts the tone of the answer
- **Document retrieval** – picks the relevant support document (refunds, billing, login, account lockout, API authentication, subscriptions, security, user management, outages)
- **Grounded answers** – Gemini answers only from the retrieved document
- **Escalation rules** – billing, refund, legal and account-compromise questions are flagged for a human
- **Handoff summary** – produces a structured summary (persona, issue, documents used, recommendation) for the human agent

## Tech stack

Python 3 · Google Gemini API (`google-generativeai`) · python-dotenv

## Getting started

```bash
git clone https://github.com/rajkumarprog/support-agent-gemini.git
cd support-agent-gemini

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your free key from [Google AI Studio](https://aistudio.google.com/):

```
GEMINI_API_KEY=your_api_key_here
```

Run it **from the project root**:

```bash
python src/app.py
```

### Example

```
Enter your name: Priya
Ask a question: I want a refund for last month

Detected Persona: Business Executive
Retrieved Source: refund_policy.txt
Answer: ...
ESCALATION REQUIRED
Handoff Summary: {'persona': 'Business Executive', 'issue': 'I want a refund for last month', ...}
```

## Project structure

```
src/
  app.py                 # CLI entry point
  docs/
    persona.py           # persona detection
    retrieval.py         # keyword-based document retrieval
    escalation.py        # escalation rules
    handoff.py           # human handoff summary
    *.txt                # support knowledge-base documents
```

## Limitations and next steps

- Persona detection and retrieval are keyword-based; embeddings would handle paraphrased questions better
- Add unit tests for persona, retrieval and escalation logic
- Wrap the agent in a small web API or UI

## Author

**Rajkumar Panikera** · [LinkedIn](https://www.linkedin.com/in/rajkumar-panikera-a083ab1a5) · [GitHub](https://github.com/rajkumarprog)
