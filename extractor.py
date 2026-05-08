import os
from PyPDF2 import PdfReader


def extract_text(file_path):

    # Get absolute path
    absolute_path = os.path.abspath(file_path)

    # Check file exists
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"File not found: {absolute_path}")

    # Get file extension
    file_extension = file_path.split(".")[-1].lower()

    # PDF Extraction
    if file_extension == "pdf":

        reader = PdfReader(absolute_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    # TXT Extraction
    elif file_extension == "txt":

        with open(absolute_path, "r", encoding="utf-8") as file:
            return file.read()

    else:
        raise ValueError("Unsupported file type")