import os
import smtplib
import ssl
from email.message import EmailMessage
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender_email, receiver_email, subject, body, server='smtp.gmail.com', port=465):
    # Get the password securely
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not gmail_app_password:
        logging.error("GMAIL_APP_PASSWORD environment variable not set.")
        return

    # Create the email message
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.set_content(body)

    # Set up the SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(server, port, context=context) as smtp:
            smtp.login(sender_email, gmail_app_password)
            smtp.sendmail(sender_email, receiver_email, email.as_string())
            logging.info("Email sent successfully.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")

if __name__ == "__main__":
    sender_email = os.environ.get("SENDER_EMAIL", 'default_sender@gmail.com')
    receiver_email = os.environ.get("RECEIVER_EMAIL", 'default_receiver@gmail.com')
    
    # Get user inputs for the subject and body
    subject = input("Please enter the subject of the email: ")
    print("Please enter the body of the email. Enter 'END' on a new line to finish:")
    input_lines = []
    while True:
        line = input()
        if line == "END":
            break
        input_lines.append(line)
    body = "\n".join(input_lines)

    send_email(sender_email, receiver_email, subject, body)
