"""
Mock AI Analyzer Module
"""

def analyze_text(text):

    findings = []

    # Convert text to lowercase
    text = text.lower()

    # Simple rule checks
    if "missing" in text:
        findings.append("Potential issue detected: Missing information found.")

    if "pending" in text:
        findings.append("Compliance warning: Pending status identified.")

    if "fraud" in text:
        findings.append("Critical alert: Possible fraud-related content.")

    if "error" in text:
        findings.append("System error reference detected.")

    # Default message
    if not findings:
        findings.append("No major audit issues detected.")

    return findings