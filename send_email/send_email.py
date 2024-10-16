import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # SMTP server details for Gmail (change these for another provider)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure connection with the server using SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable security (TLS)
        server.login(sender_email, sender_password)  # Log in to the SMTP server

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Always close the server connection
        server.quit()

# Example usage
if __name__ == "__main__":
    sender_email = "youremail@gmail.com"
    sender_password = "yourpassword"  # Use app password for Gmail if 2FA is enabled
    recipient_email = "recipientemail@example.com"
    subject = "Dynamic Email Subject"
    body = "This is a dynamic email sent using Python."

    send_email(sender_email, sender_password, recipient_email, subject, body)
