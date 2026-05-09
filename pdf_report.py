from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(report_text, output_path):

    try:

        document = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        elements = []

        lines = report_text.split("\n")

        for line in lines:

            paragraph = Paragraph(line, styles["BodyText"])

            elements.append(paragraph)

            elements.append(Spacer(1, 10))

        document.build(elements)

        print(f"PDF report created: {output_path}")

    except Exception as error:

        print(f"PDF Generation Error: {error}")