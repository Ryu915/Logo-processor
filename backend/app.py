from flask import Flask, request, jsonify
from flask_cors import CORS
from processor import generate_grayscale, generate_border, generate_silhouette
from email_service import send_email
from flask import send_from_directory
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/process", methods=["POST"])
def process_image():

    if "image" not in request.files:
        return jsonify({"error": "no image uploaded"}), 400
    
    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "empty file name"}), 400
    
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    # Processing

    # Grayscale
    grayscale_path = os.path.join("outputs", "grayscale.png")
    gray_image = generate_grayscale(filepath, grayscale_path)

    # Border
    border_path = os.path.join("outputs", "border.png")
    generate_border(gray_image, border_path)

    # Silhouette
    silhouette_path = os.path.join("outputs", "silhouette.png")
    generate_silhouette(gray_image, silhouette_path)

    # Send email
    attachments = [
        grayscale_path,
        border_path,
        silhouette_path
    ]

    try:
        send_email(attachments)
        email_status = "sent"
    except Exception as e:
        print(e)
        email_status = "failed"

    return jsonify({
    "message": "Image processed successfully",
    "filename": file.filename,
    "grayscale": "http://127.0.0.1:5001/outputs/grayscale.png",
    "border": "http://127.0.0.1:5001/outputs/border.png",
    "silhouette": "http://127.0.0.1:5001/outputs/silhouette.png",
    "email_status": email_status
})
    
@app.route("/outputs/<filename>")
def get_output_file(filename):

    return send_from_directory("outputs", filename)

@app.route("/")
def home():
    return "Flask server running"

if __name__ == "__main__":
    app.run(debug=True, port=5001)