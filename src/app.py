import os

import google.generativeai as genai
from dotenv import load_dotenv

from docs.escalation import should_escalate
from docs.handoff import create_handoff
from docs.persona import detect_persona
from docs.retrieval import retrieve_document

# Tone guidance for each detected persona, so answers actually adapt to the user.
PERSONA_TONE = {
    "Technical Expert": "Be precise and technical. Include exact steps and settings.",
    "Frustrated User": "Be calm and empathetic. Acknowledge the problem first, then give short, simple steps.",
    "Business Executive": "Be brief and outcome-focused. Lead with the answer and its impact.",
}


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY is missing. Copy .env.example to .env and add your key.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    name = input("Enter your name: ")
    print("Welcome", name)

    question = input("Ask a question: ").strip()
    if not question:
        print("Please enter a question.")
        return

    persona = detect_persona(question)
    print("\nDetected Persona:", persona)

    doc_name, doc_content = retrieve_document(question)

    if doc_name is None:
        print("\nNo matching support document was found for this question.")
    else:
        print("\nRetrieved Source:", doc_name)

        prompt = f"""
You are a customer support agent.

Tone: {PERSONA_TONE.get(persona, "")}

Use ONLY the following support document. If it does not answer the question,
say so and suggest contacting support.

Document:
{doc_content}

Question:
{question}
"""
        response = model.generate_content(prompt)
        print("\nAnswer:")
        print(response.text)

    if should_escalate(question) or doc_name is None:
        print("\nESCALATION REQUIRED")
        print("\nHandoff Summary:")
        print(create_handoff(persona, question, doc_name))


if __name__ == "__main__":
    main()
