import os
import re

# Folder that holds the knowledge-base .txt files (this file's folder), so the
# app works no matter which directory it is started from.
DOCS_DIR = os.path.dirname(os.path.abspath(__file__))

# Checked in order: the first keyword found in the question decides the document.
MAPPING = [
    ("refund", "refund_policy.txt"),
    ("billing", "billing_policy.txt"),
    ("invoice", "billing_policy.txt"),
    ("password", "password_reset.txt"),
    ("lock", "account_lockout.txt"),
    ("login", "login_troubleshooting.txt"),
    ("log in", "login_troubleshooting.txt"),
    ("api", "api_authentication.txt"),
    ("authentication", "api_authentication.txt"),
    ("subscription", "subscription_faq.txt"),
    ("security", "security_policy.txt"),
    ("outage", "service_outage.txt"),
    ("user", "user_management.txt"),
]


def find_document(question):
    """Return the file name of the best-matching document, or None."""
    q = question.lower()
    for keyword, filename in MAPPING:
        # \b stops "api" matching inside words like "rapid"
        if re.search(r"\b" + re.escape(keyword), q):
            return filename
    return None


def retrieve_document(question):
    filename = find_document(question)
    if filename is None:
        return None, "No relevant document found."

    with open(os.path.join(DOCS_DIR, filename), "r", encoding="utf-8") as file:
        return filename, file.read()
