import os

from extractor import extract_text
from analyzer import analyze_text
from risk_engine import calculate_risk
from report_generator import generate_report, save_report
from pdf_report import create_pdf_report
from nlp_analyzer import nlp_analyze


# Folder paths
DOCUMENTS_FOLDER = "documents"
REPORTS_FOLDER = "reports"
PDF_REPORTS_FOLDER = "pdf_reports"


if __name__ == "__main__":

    try:

        # Get all files from documents folder
        files = os.listdir(DOCUMENTS_FOLDER)

        # Filter only PDF files
        pdf_files = [
            file for file in files
            if file.endswith(".pdf")
        ]

        # Process each PDF
        for pdf_file in pdf_files:

            file_path = os.path.join(
                DOCUMENTS_FOLDER,
                pdf_file
            )

            print(f"\nProcessing: {pdf_file}")

            # Extract text
            text = extract_text(file_path)

            # Analyze text
            # NLP Analyze text
            findings = nlp_analyze(text)

            # Calculate risk
            risk_score = calculate_risk(findings)

            # Generate report
            report = generate_report(
                findings,
                risk_score
            )

            # ---------- TEXT REPORT ----------

            report_name = pdf_file.replace(
                ".pdf",
                "_report.txt"
            )

            report_path = os.path.join(
                REPORTS_FOLDER,
                report_name
            )

            save_report(report, report_path)

            # ---------- PDF REPORT ----------

            pdf_name = pdf_file.replace(
                ".pdf",
                "_report.pdf"
            )

            pdf_path = os.path.join(
                PDF_REPORTS_FOLDER,
                pdf_name
            )

            create_pdf_report(report, pdf_path)

            # Display report
            print(report)

    except Exception as error:

        print(f"Error: {error}")