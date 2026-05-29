# Logo Processing & Email Delivery System

A full-stack backend service that processes uploaded logos using computer vision, generates multiple transformations, and automatically emails the results — fully automated after upload.

---

##  Features

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

##  Tech Stack

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

##  Project Structure
