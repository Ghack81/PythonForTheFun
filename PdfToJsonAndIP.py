from flask import Flask, request, jsonify
import os
import json
import PyPDF2
import requests

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
        pdf_data["metadata"] = pdf_reader.metadata
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

    # Get user's IP address
    user_ip = request.remote_addr
    json_data["ip"] = user_ip

    # Get user's geolocation based on IP
    geolocation = get_geolocation(user_ip)
    json_data["geolocation"] = geolocation

    return json_data

def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        return {
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }
    except Exception as e:
        print(f"Error fetching geolocation for IP {ip}: {e}")
        return {}

if __name__ == "__main__":
    app.run(debug=True)
