import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, to_email):
    sender_email = "jarvis112000@gmail.com"
    sender_password = "okjzplzfbcsbunro"
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Use TLS for security
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Email Sent Succesfully")
