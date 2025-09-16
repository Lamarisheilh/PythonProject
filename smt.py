import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart("Hello from Python !")
msg["Subject"] = "Reminder"
msg["From"] = "you@gmail.com"
msg["To"] = "friend@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("you@gmail.com", "app_password")
    server.send_message(msg)
