import smtplib
import getpass
import mimetypes
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

    def add_attachment(self,file):
        file_name = file
        attachment = Path(file_name)
        print(attachment)
        mime_type, _ = mimetypes.guess_type(file_name)
        if mime_type is None:
            main_type = "application"
            sub_type = "octet-stream"
        else:
            main_type , sub_type = mime_type.split('/',1)
        try:
            if attachment.exists():
                self.msg.add_attachment(
                    attachment.read_bytes(),
                    maintype = main_type,
                    subtype = sub_type,
                    filename = attachment.name
                )
            else: 
                print(f"{file_name} does not exist in your system")
        except Exception as e:
            print(f"An error was orccured as {e}")




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
    while True:
        print("select from the given options!")
        print("1 send an email\n2 send email to multiple recipients\n3 Exit")
        try:
            choice = int(input("Enter the option(1,2 or 3): "))
        except ValueError:
            print("Enter the correct type of choice")

        if choice == 1:
            subject = input("Enter the subject for you mail: ")
            text_content = input("Enter the text: ")
            email.message_body(subject)
            email.plain_text(text_content)
            print("Enter Y if you want to add an attachment N for not wanting it ..")
            option = input("Enter your option: ").upper()
            if option == "Y":
                file_name = input("enter the file name: ")
                email.add_attachment(file_name)
            elif option == "N":
                print("OK understood")
            else: 
                print("Please enter the correct option next time")
                break
            email.smtp_connection()


        elif choice == 2:
            pass

        elif choice == 3:
            break

        else:
            print("Entered the wrong option!")
main()

        