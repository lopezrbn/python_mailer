import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


PATH_EMAIL_CREDENTIALS = "<path_to_email_credentials>"  # Path to the JSON file with email credentials


def send_email(credentials:dict=PATH_EMAIL_CREDENTIALS, email_to:str="", subject:str="", message:str=""):

    # Load the email credentials
    with open(PATH_EMAIL_CREDENTIALS, "r") as f:
        credentials = json.load(f)

    # Retrieve the email credentials
    email_from = credentials["email_from"]
    password = credentials["password"]

    # Configuration for the SMTP server    
    if email_from.endswith("@gmail.com"):
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465
        use_ssl = True      # Gmail uses SSL
    else:
        SMTP_SERVER = "smtp.office365.com"
        SMTP_PORT = 587
        use_ssl = False     # Office365 uses TLS

    # Create message
    msg = MIMEMultipart("alternative")
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))
    
    # Send the email
    try:
        if use_ssl:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(email_from, password)
                server.sendmail(email_from, email_to, msg.as_string())
        else:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(email_from, password)
                server.sendmail(email_from, email_to, msg.as_string())
        print(f'Email "{subject}" sent successfully.')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_email(
        email_to="<email_to>",
        subject="Test email",
        message="This is a test email"
    )