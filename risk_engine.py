"""
Risk Engine Module
"""

def calculate_risk(findings):

    risk_score = 0

    for finding in findings:

        finding = finding.lower()

        if "critical" in finding:
            risk_score += 50

        elif "missing" in finding:
            risk_score += 20

        elif "warning" in finding:
            risk_score += 10

        elif "unauthorized" in finding:
            risk_score += 40

        elif "error" in finding:
            risk_score += 15

    # Maximum limit
    if risk_score > 100:
        risk_score = 100

    return risk_score