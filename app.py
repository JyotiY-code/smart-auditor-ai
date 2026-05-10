import os
from extractor import extract_text
from nlp_analyzer import nlp_analyze
from risk_engine import calculate_risk
from report_generator import generate_report

from flask import Flask, render_template, request


app = Flask(__name__)

UPLOAD_FOLDER = "documents"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    if "pdf_file" not in request.files:

        return "No file uploaded."

    file = request.files["pdf_file"]

    if file.filename == "":

        return "No selected file."

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)

    # Extract text
    text = extract_text(file_path)

    # NLP analysis
    findings = nlp_analyze(text)

    # Risk scoring
    risk_score = calculate_risk(findings)

    # Generate report
    report = generate_report(
        findings,
        risk_score
    )

    return f"""
    <h1>Audit Completed</h1>

    <pre>{report}</pre>

    <br>

    <a href="/">
        Analyze Another PDF
    </a>
    """

if __name__ == "__main__":

    app.run(debug=True)