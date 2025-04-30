import os
import json
from typing import Union
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(
    credentials: Union[str, dict, None] = None,
    email_to: str = None,
    subject: str = None,
    body: str = None
):
    """
    Send an email using SMTP with credentials provided via a JSON file,
    a dictionary, or an environment variable.

    Parameters:
        - credentials (str | dict | None): Either:
            - A dictionary with 'email_from' and 'password' keys,
            - A path to a JSON file with those keys,
            - Or None to load the path from the environment variable
              'PATH_EMAIL_CREDENTIALS'.
        - email_to (str): Recipient email address. If not provided,
          it will be taken from the credentials dictionary.
        - subject (str): Email subject.
        - body (str): Plain-text body of the email.

    Raises:
        ValueError: If credentials are missing or improperly formatted.

    Example:
        send_email(
            credentials="path/to/credentials.json",
            email_to="recipient@example.com",
            subject="Test Email",
            message="Hello from Python!"
        )
    """

    # If credentials is None, try to load path from environment variable
    if credentials is None:
        PATH_EMAIL_CREDENTIALS = os.getenv("PATH_EMAIL_CREDENTIALS")
        if PATH_EMAIL_CREDENTIALS is None:
            raise ValueError(
                "No credentials provided and PATH_EMAIL_CREDENTIALS "
                "environment variable is not set."
            )
        else:
            with open(PATH_EMAIL_CREDENTIALS, "r") as f:
                credentials = json.load(f)

    # If credentials is a string, treat it as a path to a JSON file
    elif isinstance(credentials, str):
        if os.path.exists(credentials):
            with open(credentials, "r") as f:
                credentials = json.load(f)
        else:
            raise ValueError(
                f"Credentials file {credentials} does not exist."
            )

    # If credentials is a dictionary, use it directly
    elif isinstance(credentials, dict):
        pass

    # Invalid credentials type
    else:
        raise ValueError(
            "Credentials must be a string (path to JSON file), a dictionary, "
            "or None."
        )

    # Extract credentials from dictionary
    email_from = credentials["email_from"]
    password = credentials["password"]
    if not email_to:
        email_to = credentials.get("email_to", None)
        if not email_to:
            raise ValueError("Recipient email address (email_to) is required.")

    # Configure SMTP server based on email domain
    if email_from.endswith("@gmail.com"):
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465
        use_ssl = True  # Gmail requires SSL
    else:
        SMTP_SERVER = "smtp.office365.com"
        SMTP_PORT = 587
        use_ssl = False  # Office365 uses TLS

    # Create MIME email message
    msg = MIMEMultipart("alternative")
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the email using SSL or TLS depending on provider
    try:
        if use_ssl:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(email_from, password)
                server.sendmail(
                    email_from, email_to, msg.as_string()
                )
        else:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(email_from, password)
                server.sendmail(
                    email_from, email_to, msg.as_string()
                )
        print(f'Email "{subject}" sent successfully.')
    except Exception as e:
        print(f"Error: {e}")


# Example usage if executed directly (for testing or CLI execution)
if __name__ == "__main__":
    send_email(
        credentials="path/to/credentials.json",  # str with path to credentials file or a dictionary with the credentials or None to use env var
        email_to="example@example.com",
        subject="Test email",
        message="This is a test email"
    )