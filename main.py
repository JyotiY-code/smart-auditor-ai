import os

from extractor import extract_text
from analyzer import analyze_text
from risk_engine import calculate_risk
from report_generator import generate_report, save_report


DOCUMENTS_FOLDER = "documents"
REPORTS_FOLDER = "reports"


if __name__ == "__main__":

    try:

        # Get all PDF files
        files = os.listdir(DOCUMENTS_FOLDER)

        pdf_files = [file for file in files if file.endswith(".pdf")]

        # Process each PDF
        for pdf_file in pdf_files:

            file_path = os.path.join(DOCUMENTS_FOLDER, pdf_file)

            print(f"\nProcessing: {pdf_file}")

            # Extract text
            text = extract_text(file_path)

            # Analyze text
            findings = analyze_text(text)

            # Calculate risk
            risk_score = calculate_risk(findings)

            # Generate report
            report = generate_report(findings, risk_score)

            # Create report filename
            report_name = pdf_file.replace(".pdf", "_report.txt")

            report_path = os.path.join(REPORTS_FOLDER, report_name)

            # Save report
            save_report(report, report_path)

            print(report)

    except Exception as e:
        print("Error:", e)