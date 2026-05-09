"""
Professional Report Generator
"""


def generate_report(findings, risk_score):

    report = "\n===== SMART AUDIT REPORT =====\n"

    report += "\nDetected Issues:\n"

    for index, finding in enumerate(findings, start=1):
        report += f"{index}. {finding}\n"

    # Risk Classification
    if risk_score >= 70:
        risk_level = "HIGH"

    elif risk_score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    report += f"\nRisk Score: {risk_score}/100\n"
    report += f"Risk Level: {risk_level}\n"

    # Summary Section
    report += "\nSummary:\n"

    if risk_level == "HIGH":
        report += (
            "Critical audit anomalies detected. "
            "Immediate review recommended.\n"
        )

    elif risk_level == "MEDIUM":
        report += (
            "Moderate compliance concerns detected. "
            "Further inspection advised.\n"
        )

    else:
        report += (
            "No major audit risks identified.\n"
        )

    return report


def save_report(report, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"\nReport saved successfully as: {filename}")