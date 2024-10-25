import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Set up the MIME
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject

    # Attach the message to the MIME
    email_message.attach(MIMEText(message, 'plain'))

    # Create SMTP session
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            # Login to the sender's email
            server.login(sender_email, sender_password)
            # Send the email
            server.send_message(email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    sender_email = input("Enter your Gmail address: ")
    sender_password = getpass.getpass("Enter your Gmail password or app password: ")
    receiver_email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")

    send_email(sender_email, sender_password, receiver_email, subject, message)

if __name__ == "__main__":
    main()
