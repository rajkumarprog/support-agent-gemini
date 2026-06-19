def detect_persona(message):

    msg = message.lower()

    if any(word in msg for word in
           ["api", "logs", "configuration", "authentication"]):
        return "Technical Expert"

    elif any(word in msg for word in
             ["frustrated", "angry", "nothing works", "tried everything"]):
        return "Frustrated User"

    else:
        return "Business Executive"