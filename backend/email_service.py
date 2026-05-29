import smtplib
import os

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_email(attachments):
    msg = EmailMessage()

    msg["Subject"] = "Processed Logo Output Results"
    msg["FROM"] = EMAIL_ADDRESS
    msg["TO"] = RECIPIENT_EMAIL

    msg.set_content("Attached are the processed outputs.")

    for file_path in attachments:
        with open(file_path, "rb") as file:
            file_data = file.read()
            file_name = os.path.basename(file_path)
        
        msg.add_attachment(
            file_data,
            maintype="image",
            subtype="png",
            filename=file_name
        )
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)