# auto_email
# Email Sender App

This is a simple web application built using Streamlit that allows users to send emails to multiple recipients. It uses the `smtplib` library for sending emails via SMTP.

## Features

- Send emails to multiple recipients simultaneously.
- Securely input email credentials within the app.
- User-friendly interface for composing and sending emails.

## Requirements

- Python 3.6 or higher
- Streamlit

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/email-sender-app.git
2. Navigate to the project directory.

   ```bash
   cd email-sender-app
3. Create and activate a virtual environment (optional but recommended).
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
4. Install the required packages.
    ```bash
    pip install -r requirements.txt
5. Alternatively, you can install the dependencies manually:
   ```bash
   pip install streamlitUsage
6. Run the Streamlit app.
    ```bash
    streamlit run app.py
    
Open your web browser and go to the following URL:
http://localhost:8501
Use the web interface to input your email credentials, the recipients' email addresses, and the content of the email (subject and body).

Click the "Send Emails" button to send the email to all listed recipients.

Important Notes
Gmail Users: If you are using a Gmail account, ensure that you have enabled "Less secure app access" in your Google account settings, or use an App Password if 2-Step Verification is enabled.
Recipient List: Enter multiple recipient email addresses separated by commas in the "Recipient Emails" field.
Security: Be cautious about entering your email credentials directly into the app. Consider using environment variables or more secure methods for handling passwords in production environments.
Troubleshooting
If the email fails to send, ensure that:
The email credentials are correct.
The recipient email addresses are valid.
Your internet connection is stable.
Gmail users have enabled access for less secure apps or are using an App Password.
