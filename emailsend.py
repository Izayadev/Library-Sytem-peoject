from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path
import smtplib
msg = MIMEMultipart()
msg["from"] = input("From : ")
msg["to"] = input("Enter Email : ")
msg["subject"]= input("Subject : ")

msg.attach(MIMEText("Body"))
msg.attach(Path("/home/izy/Desktop/Library System/All Book Export Report (24 of 01 ).xlsx").read_bytes)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("izayadev@gmail.com", "khppgaxxgnwvaxer")
	smtp.send_message(msg)
	print("Sent...")
