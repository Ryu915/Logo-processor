from flask import Flask, request, jsonify
from flask_cors import CORS
from processor import generate_grayscale, generate_border, generate_silhouette
from email_service import send_email
from flask import send_from_directory
import shutil
import threading
import time
import uuid
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/process", methods=["POST"])
def process_image():
    session_id = str(uuid.uuid4())

    upload_dir = os.path.join("uploads", session_id)
    output_dir = os.path.join("outputs", session_id)

    os.makedirs(upload_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    if "image" not in request.files:
        return jsonify({"error": "no image uploaded"}), 400
    
    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "empty file name"}), 400
    
    filepath = os.path.join(upload_dir, file.filename)
    file.save(filepath)

    # Processing

    # Grayscale
    grayscale_path = os.path.join(output_dir, "grayscale.png")
    gray_image = generate_grayscale(filepath, grayscale_path)

    # Border
    border_path = os.path.join(output_dir, "border.png")
    generate_border(gray_image, border_path)

    # Silhouette
    silhouette_path = os.path.join(output_dir, "silhouette.png")
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

    threading.Thread(
        target=delayed_cleanup,
        args=(upload_dir, output_dir)
    ).start()

    return jsonify({
        "message": "Image processed successfully",
        "session_id": session_id,
        "filename": file.filename,
        "email_status": email_status
    })
    
def delayed_cleanup(upload_dir, output_dir, delay=60):
    time.sleep(delay)
    shutil.rmtree(upload_dir)
    shutil.rmtree(output_dir)

@app.route("/outputs/<session_id>/<filename>")
def get_output_file(session_id, filename):
    return send_from_directory(
        os.path.join("outputs", session_id),
        filename
    )

@app.route("/")
def home():
    return "Flask server running"

if __name__ == "__main__":
    app.run(debug=True, port=5001)