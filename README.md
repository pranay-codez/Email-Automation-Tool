# 📧 Email Automation Tool

A command-line Email Automation Tool built with Python that can send emails to one or multiple recipients, with optional file attachments.

This project was built as part of my AI Automation & Business Systems learning journey to understand how Python can automate real-world communication tasks using SMTP.

---

## 🚀 Features

- Send emails using Gmail SMTP
- Send to multiple recipients
- Add custom subject and message
- Attach files to emails
- Secure password input using `getpass`
- Automatic MIME type detection for attachments
- Basic exception handling for authentication and runtime errors
- Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python
- smtplib
- email.message
- getpass
- pathlib
- mimetypes

---

## 📂 Project Structure

```
Email-Automation/
│
├── email_automation.py
├── README.md
```

---

## ⚙️ How It Works

1. Enter the sender's Gmail address.
2. Enter the Gmail App Password.
3. Add one or more recipient email addresses.
4. Enter the email subject.
5. Enter the email body.
6. Optionally attach a file.
7. The email is sent through Gmail's SMTP server.

---

## 📌 Requirements

- Python 3.x
- Gmail account
- Gmail App Password enabled

---

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Email-Automation
```

Run the program:

```bash
python email_automation.py
```

---

## 📚 What I Learned

Through this project I learned:

- How SMTP works
- Sending emails with Python
- Working with the `EmailMessage` class
- Adding file attachments using MIME types
- Secure password handling with `getpass`
- Using `pathlib` for file management
- Structuring a Python project using classes and methods
- Exception handling for real-world applications

---

## 🔮 Future Improvements

- HTML email support
- Email templates
- Read recipients from CSV or Excel
- Email scheduling
- Logging system
- Graphical User Interface (GUI)

---

## 👨‍💻 Author

**Pranay**

Building AI Automation, AI Agents, and Business Systems one project at a time.