from dotenv import load_dotenv
import os
import google.generativeai as genai

from docs.persona import detect_persona
from docs.escalation import should_escalate
from docs.handoff import create_handoff
from docs.retrieval import retrieve_document

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

name = input("Enter your name: ")
print("Welcome", name)

question = input("Ask a question: ")

persona = detect_persona(question)

print("\nDetected Persona:", persona)

doc_name, doc_content = retrieve_document(question)

print("\nRetrieved Source:", doc_name)

prompt = f"""
You are a customer support agent.

Use ONLY the following support document.

Document:
{doc_content}

Question:
{question}
"""

response = model.generate_content(prompt)

print("\nAnswer:")
print(response.text)

if should_escalate(question):
    print("\nESCALATION REQUIRED")

    handoff = create_handoff(
        persona,
        question,
        doc_name
    )

    print("\nHandoff Summary:")
    print(handoff)