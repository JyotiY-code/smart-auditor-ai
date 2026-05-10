"""
Smart NLP Analyzer
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Download required data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# Risk-related keywords
RISK_WORDS = [
    "fraud",
    "scam",
    "money laundering",
    "corruption",
    "bribe",
    "fake",
    "illegal",
    "suspicious",
    "forged",
    "unauthorized"
]


def nlp_analyze(text):

    findings = []

    # Convert to lowercase
    text = text.lower()

    # Tokenize words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))

    filtered_words = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]

    # Detect suspicious terms
    for risk_word in RISK_WORDS:

        if risk_word in text:
            findings.append(
                f"Potential risk detected: {risk_word}"
            )

    # No findings
    if not findings:

        findings.append(
            "No major audit issues detected."
        )

    return findings