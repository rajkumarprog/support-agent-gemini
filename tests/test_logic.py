"""Unit tests for the rule-based parts of the agent (no API key needed)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from docs.escalation import should_escalate  # noqa: E402
from docs.handoff import create_handoff  # noqa: E402
from docs.persona import detect_persona  # noqa: E402
from docs.retrieval import find_document, retrieve_document  # noqa: E402


def test_persona_detection():
    assert detect_persona("My API returns 401 errors") == "Technical Expert"
    assert detect_persona("I'm frustrated, nothing works") == "Frustrated User"
    assert detect_persona("What does the premium plan cost?") == "Business Executive"


def test_retrieval_picks_expected_document():
    assert find_document("I want a refund") == "refund_policy.txt"
    assert find_document("I forgot my password") == "password_reset.txt"
    assert find_document("My account is locked") == "account_lockout.txt"
    assert find_document("How do I add a new user?") == "user_management.txt"


def test_retrieval_uses_word_boundaries():
    # "rapid" contains "api" but is not about the API
    assert find_document("rapid growth plans") is None


def test_retrieve_document_reads_file_from_any_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    name, content = retrieve_document("refund please")
    assert name == "refund_policy.txt"
    assert content.strip()


def test_no_document_found():
    assert retrieve_document("hello there") == (None, "No relevant document found.")


def test_escalation_rules():
    assert should_escalate("I need a refund")
    assert should_escalate("my account hacked yesterday")
    assert not should_escalate("how do I reset my password")


def test_handoff_summary():
    h = create_handoff("Frustrated User", "Billing issue", "billing_policy.txt")
    assert h["persona"] == "Frustrated User"
    assert h["documents_used"] == ["billing_policy.txt"]
