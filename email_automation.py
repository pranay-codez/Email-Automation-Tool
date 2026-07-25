import smtplib
import getpass
from email.message import EmailMessage
from pathlib import Path

class Email_Automation:
    # taking in the credentials
    def __init__(self,receiver_mail):
        self.senders_mail = "menonpranay54@gmail.com"
        self.receiver_mail = receiver_mail
        self.password = getpass.getpass("Enter your password: ")
    # definig message structure
    def message_body(self,subject):
        self.msg = EmailMessage()
        self.msg["Subject"] = subject
        self.msg["From"] = self.senders_mail
        self.msg["To"] = self.receiver_mail

    def plain_text(self,text):
        self.msg.set_content(text)

    # setting up the smtp server
    def smtp_connection(self):
        smtp_server = "smtp.gmail.com"
        port = 587

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(self.senders_mail , self.password)
                server.send_message(self.msg)
                print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("authentication failed check your mail and app password")
        except Exception as e:
            print(f"{e}")

        


def main():
    receiver_email = input("Enter the receiver mail address: ").lower()
    email = Email_Automation(receiver_email)
    subject = input("Enter the subject for you mail: ")
    text_content = input("Enter the text: ")
    email.message_body(subject)
    email.plain_text(text_content)
    email.smtp_connection()
main()

        