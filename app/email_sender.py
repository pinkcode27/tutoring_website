import smtplib
import ssl
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app import app
from concurrent.futures import ThreadPoolExecutor


class EmailMessage:
    """
    Represents an email message.

    Attributes:
        sender_name (str): The name of the sender.
        sender_email (str): The email address of the sender.
        subject (str): The subject of the email.
        message (str): The body message of the email.
    """

    def __init__(self, sender_name, sender_email, subject, message):
        """
        Initialize an EmailMessage object.

        Args:
            sender_name (str): The name of the sender.
            sender_email (str): The email address of the sender.
            subject (str): The subject of the email.
            message (str): The body message of the email.
        """
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.subject = subject
        self.message = message

    def create_message(self):
        """
        Create a MIME message for the email.

        Returns:
            MIMEMultipart: A MIME message object representing the email.
        """
        msg = MIMEMultipart()
        msg['From'] = f'{self.sender_name} <{self.sender_email}>'
        msg['To'] = f'{self.sender_email}'
        msg['Subject'] = self.subject
        message = f'''
                Name: {self.sender_name}\n
                Email: {self.sender_email}\n
                Message: {self.message}
                '''
        msg.attach(MIMEText(message, 'plain'))
        return msg


class EmailSender:
    """
    Sends email messages using SMTP.

    Attributes:
        sender_email (str): The email address of the sender.
        sender_password (str): The password of the sender's email account.
    """

    def __init__(self, sender_email, sender_password):
        """
        Initialize an EmailSender object.

        Args:
            sender_email (str): The email address of the sender.
            sender_password (str): The password of the sender's email account.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, email_message):
        """
        Send an email message.

        Args:
            email_message (EmailMessage): The EmailMessage object to be sent.

        Raises:
            Exception: If there is an error while sending the email.
        """
        def send():
            msg = email_message.create_message()

            try:
                with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as connection:
                    connection.starttls(context=app.config['CONTEXT'])
                    connection.login(user=self.sender_email, password=self.sender_password)
                    connection.sendmail(from_addr=self.sender_email, to_addrs=[email_message.sender_email],
                                        msg=msg.as_string())
            except smtplib.SMTPException as e:
                logging.error(f'SMTP Error: {e}')
            except Exception as e:
                logging.error(f'Error sending email: {e}')

        with ThreadPoolExecutor() as executor:
            executor.submit(send)
