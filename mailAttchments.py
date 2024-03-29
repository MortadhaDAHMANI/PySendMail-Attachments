import email, smtplib, ssl, os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "mortadha.dahmani@gmail.com"  # Enter your address
receiver_email = "john.doe@gmail.com"  # Enter receiver address
password = input("Type your password and press enter:")


# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

#current_dir = os.path.dirname(os.path.realpath(__file__))
#filename = os.path.join(current_dir, "contact.csv").replace("\\","/")

filename="contact.csv"

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()
##print(text)
# Log in to server using secure context and send email

try:
    with smtplib.SMTP("ssl0.ovh.net", 587) as server:
        server.starttls()
        server.login(login_email, password)
        server.sendmail(sender_email, receiver_email, text)
except :
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    
#'''
