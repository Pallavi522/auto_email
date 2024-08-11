import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import streamlit as st


# Function to send email
def send_email(sender_email, password, recipient_email, subject, body):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server
        smtp_server = "smtp.gmail.com"
        port = 587
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        return True
    except Exception as e:
        st.error(f"Error sending email to {recipient_email}: {e}")
        return False

# Streamlit interface
st.title("Email Sender App")

# Input fields for email credentials
sender_email = st.text_input("Your Email", type="default")
password = st.text_input("Your Password", type="password")

# Text area for recipients
recipients = st.text_area("Recipient Emails (comma-separated)", "")

# Input fields for email content
subject = st.text_input("Subject")
body = st.text_area("Email Body")

# Send emails
if st.button("Send Emails"):
    recipient_list = [email.strip() for email in recipients.split(',')]
    for recipient in recipient_list:
        if send_email(sender_email, password, recipient, subject, body):
            st.success(f"Email successfully sent to {recipient}")
        else:
            st.error(f"Failed to send email to {recipient}")
