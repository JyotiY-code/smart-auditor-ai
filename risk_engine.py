"""
Risk Scoring Engine
"""


def calculate_risk(findings):

    risk_score = 0

    for finding in findings:

        finding = finding.lower()

        if "fraud" in finding:
            risk_score += 40

        elif "money laundering" in finding:
            risk_score += 50

        elif "corruption" in finding:
            risk_score += 35

        elif "suspicious" in finding:
            risk_score += 25

        elif "illegal" in finding:
            risk_score += 30

        elif "fake" in finding:
            risk_score += 20

    # Limit max score
    risk_score = min(risk_score, 100)

    return risk_score