from flask import Flask, request, jsonify
import os
import json
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf_file = request.files["pdf_file"]
        if pdf_file:
            pdf_path = "temp.pdf"
            pdf_file.save(pdf_path)
            pdf_data = extract_pdf_data(pdf_path)
            json_data = convert_to_json(pdf_data)
            os.remove(pdf_path)
            return jsonify(json_data)

    return """
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="pdf_file">
        <input type="submit" value="Analyser le PDF">
    </form>
    """

def extract_pdf_data(pdf_path):
    pdf_data = {}
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_data["text"] = pdf_reader.pages[0].extract_text()
        pdf_data["metadata"] = pdf_reader.getDocumentInfo()
    return pdf_data

def convert_to_json(pdf_data):
    json_data = {
        "text": pdf_data["text"],
        "metadata": {
            "author": pdf_data["metadata"].author,
            "title": pdf_data["metadata"].title,
            "subject": pdf_data["metadata"].subject,
        },
    }
    return json_data

if __name__ == "__main__":
    app.run(debug=True)
