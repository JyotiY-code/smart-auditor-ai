from extractor import extract_text
from analyzer import analyze_text
from risk_engine import calculate_risk
from report_generator import generate_report, save_report

if __name__ == "__main__":

    file_path = "sample.pdf"

    try:
        # Extract document text
        text = extract_text(file_path)

        # Analyze text
        findings = analyze_text(text)

        # Calculate risk
        risk_score = calculate_risk(findings)

        # Generate final report
        report = generate_report(findings, risk_score)

        # Display report
        print(report)
        save_report(report)

    except Exception as e:
        print("Error:", e)