"""
Hybrid Document Extractor
Supports:
1. Normal PDF text extraction
2. OCR fallback for scanned PDFs
"""

import os

import PyPDF2
import pytesseract

from PIL import Image
from pdf2image import convert_from_path


# Optional:
# Set Tesseract path manually if needed
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(file_path):

    extracted_text = ""

    try:

        # -------- NORMAL PDF EXTRACTION --------
        with open(file_path, "rb") as file:

            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

        print("Normal extraction completed.")

        # -------- OCR EXTRACTION --------
        print("Running OCR on document pages...")

        images = convert_from_path(
    file_path,
    poppler_path=r"C:\Users\ashis\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)
        for image in images:

            ocr_text = pytesseract.image_to_string(image)

            extracted_text += "\n" + ocr_text

        print("OCR extraction completed.")

        return extracted_text

    except Exception as error:

        print(f"Extraction Error: {error}")

        return ""