import os

def retrieve_document(question):

    question = question.lower()

    mapping = {
        "refund": "refund_policy.txt",
        "billing": "billing_policy.txt",
        "login": "login_troubleshooting.txt",
        "lock": "account_lockout.txt",
        "api": "api_authentication.txt",
        "authentication": "api_authentication.txt",
        "subscription": "subscription_faq.txt",
        "security": "security_policy.txt",
        "user": "user_management.txt",
        "outage": "service_outage.txt"
    }

    for keyword, filename in mapping.items():
        if keyword in question:
            filepath = os.path.join("src", "docs", filename)

            with open(filepath, "r", encoding="utf-8") as file:
                return filename, file.read()

    return None, "No relevant document found."