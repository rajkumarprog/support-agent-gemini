def create_handoff(persona, issue, document):

    return {
        "persona": persona,
        "issue": issue,
        "documents_used": [document],
        "attempted_steps": [],
        "recommendation": "Escalate to human support agent"
    }