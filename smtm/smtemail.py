import smtplib
from email.mime.text import MIMs

msg = MIMEText("Hello from Python !")
msg["Subject"] = "Reminder"
msg["From"] = "lamarisheilh@gmail.com"
msg["To"] = "lamarkhaled728@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("lamarisheilh@gmail.com", "app_password")
    server.send_message(msg)
