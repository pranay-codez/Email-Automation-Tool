import smtplib
import getpass
import mimetypes
from email.message import EmailMessage
from pathlib import Path

class EmailAutomation:
    # taking in the credentials
    def __init__(self, sender_email ):
        self.senders_mail = sender_email
        self.receiver_mail = []
        self.password = getpass.getpass("Enter your password: ")

    def add_recipients(self, recipients):
        self.receiver_mail = recipients.copy()
    # definig message structure
    def message_body(self,subject):
        self.msg = EmailMessage()
        self.msg["Subject"] = subject
        self.msg["From"] = self.senders_mail
        self.msg["To"] = ", ".join(self.receiver_mail)

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
    while True:
        print("select from the given options!")
        print("1 send an email\n2 Exit")
        try:
            choice = int(input("Enter the option(1 or 2): "))
        except ValueError:
            print("Enter the correct type of choice")

        if choice == 1:
            recipients = []
            sender_mail = input("Enter the sender's mail_id: ")
            email = EmailAutomation(sender_mail)
            print("How many recipients do you want to add: ")
            try:
                num = int(input("Enter: "))
                if num ==0 or num<0:
                    raise ValueError
                for i in range(num):
                    mail_id = input("Enter the mail id: ")
                    recipients.append(mail_id)
                email.add_recipients(recipients)
            except ValueError:
                print("Entered wrong type value or 0 or < 0")
                continue
            subject = input("Enter the subject for you mail: ")
            text_content = input("Enter the text: ")
            email.message_body(subject)
            email.plain_text(text_content)
            print("Enter Y if you want to add an attachment N for not wanting it ..")
            option = input("Enter your option: ").upper()
            if option == "Y":
                file_name = input("enter the file(if it didnt worked paste the whole path) name: ")
                email.add_attachment(file_name)
            elif option == "N":
                print("OK understood")
            else: 
                print("Please enter the correct option next time")
                continue
            email.smtp_connection()


        elif choice == 2:
            print("Exiting!!!")
            break

        else:
            print("Entered the wrong option!")
main()

        