# Send Email With Python

This repository contains a Python script that facilitates the sending of emails directly from the command line. Leveraging the power of Python's smtplib and email libraries, the script provides a user-friendly interface to compose and send emails with SSL encryption for enhanced security. It includes features such as loading credentials from environment variables via the python-dotenv package, robust error handling, and logging for effective troubleshooting and operational visibility. Ideal for automating email notifications, this script offers a scalable and secure solution for integrating email functionalities into Python applications.

## Getting Started 

1. Navigate to [Gmail](https://mail.google.com/mail/u/0/#inbox) and log in.
2. Click on your profile picture in the top right corner.
3. Select "Manage your Google Account" from the dropdown menu.
4. In the left-hand menu, click on "Security."
5. In the "How you sign in to Google" section, check if 2-Step Verification (2FA) is enabled. If not, enable it to proceed.
6. Visit [Gmail Apps](https://mail.google.com/mail/u/0/#inbox)
7. Under 'Select app', choose 'Other', type a custom name (e.g., Python Email App), and then click 'Generate'.
8. Copy the generated app password and paste it into your .env.example file under the GMAIL_APP_PASSWORD variable.
9. In the same .env.example file, set the SENDER_EMAIL and RECEIVER_EMAIL variables with your desired email addresses.
10. To send a pre-defined email, modify the subject and body in the send-email.py script and run it.
11. Alternatively, to send emails with dynamic content, run the send-email-dynamic-input.py script, and input the email subject and body when prompted.
