def should_escalate(question):

    q = question.lower()

    keywords = [
        "billing",
        "refund",
        "legal",
        "account hacked",
        "account compromised"
    ]

    return any(word in q for word in keywords)
