 # Logo Processing & Email Delivery System

---

## 🧾 Project Summary

A full-stack image processing system that allows users to upload logos, automatically processes them using computer vision techniques, and delivers multiple transformed outputs via email.

The system demonstrates end-to-end pipeline design including file handling, OpenCV-based image transformations, session-based processing, and automated SMTP email delivery integrated with a React frontend and Flask backend.

## 🚀 Features

- Upload PNG / JPG logos (up to 5MB)
- Automated image processing using OpenCV
  - Grayscale conversion
  - Edge / border detection (Canny)
  - Silhouette extraction (contour-based fill)
- Session-based processing (isolated workspace per upload)
- Automatic email delivery with processed outputs
- Minimal React frontend for upload + preview
- REST API backend using Flask

---

## 🧠 Tech Stack

### Backend
- Python
- Flask
- OpenCV
- NumPy
- Pillow
- Flask-CORS
- SMTP (Gmail App Passwords)

### Frontend
- React (Vite)
- JavaScript
- CSS

---

## 📦 Dependencies

### Backend

- Python 3.x
- Flask
- OpenCV (cv2)
- NumPy
- Pillow
- Flask-CORS
- SMTP (built-in Python library)

Install backend dependencies:

```bash
pip install flask opencv-python numpy pillow flask-cors
```
### Frontend

- React (Vite)
- JavaScript
- CSS

## 📁 Project Structure

```text
logo-processor/
│
├── backend/
│   ├── app.py
│   ├── processor.py
│   ├── email_service.py
│   ├── uploads/
│   ├── outputs/
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```
## 🏗️ Architecture Flow

The system follows a simple end-to-end pipeline from upload to email delivery:

```mermaid
flowchart TD
    A[User Uploads Image] --> B[React Frontend]
    B --> C[Flask API /process endpoint]
    C --> D[Save Image to Session Folder]
    D --> E[OpenCV Processing Pipeline]

    E --> E1[Grayscale Conversion]
    E --> E2[Edge Detection - Canny]
    E --> E3[Silhouette Generation]

    E1 --> F[Output Files Stored]
    E2 --> F
    E3 --> F

    F --> G[SMTP Email Service]
    G --> H[Email Sent with Attachments]

    F --> I[Temporary Cleanup]
```


## ⚙️ How It Works

1. User uploads an image from the frontend
2. Backend generates a unique session ID
3. Image is stored in a session-based folder
4. OpenCV processes the image:
   - Converts to grayscale
   - Extracts edges using Canny
   - Generates silhouette using contour fill
5. Outputs are saved in session directory
6. Backend sends all outputs via email automatically
7. Temporary files are cleaned after processing

---

## 📡 API Endpoint

### POST `/process`

Uploads an image and triggers the full processing pipeline.

---

### Request

- Content-Type: `multipart/form-data`
- Field:
  - `image` (file) → PNG / JPG image

---

### Response

```json
{
  "message": "Image processed successfully",
  "session_id": "uuid",
  "email_status": "sent"
}
```

## 🖥️ Running the Project

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/logo-processor.git
cd logo-processor
```

### 2. Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
python app.py
```

Backend runs on: 
```text
http://127.0.0.1:5001
```

### 3. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

## Email Configuration

Set environment variables:

```bash
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

Uses Gmail App Passwords for secure SMTP authentication.

## Outputs

Each upload generates:

- grayscale.png  
- border.png  
- silhouette.png  

And sends them as email attachments automatically.

---

## Key Design Decisions

- Session-based architecture to isolate uploads and avoid file collisions  
- Stateless API design for scalability  
- Separation of concerns:
  - Processing logic (OpenCV)
  - API layer (Flask)
  - Email service (SMTP module)  
- Frontend kept minimal to focus on backend + CV pipeline  

---

## Limitations

- No persistent database (intentionally kept lightweight)  
- Temporary file storage (session-based cleanup)  
- Email delivery depends on SMTP configuration  