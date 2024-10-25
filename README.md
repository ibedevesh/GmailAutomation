# Email Sender Script

A simple Python script to send emails using Gmail's SMTP service. This script allows users to send plain-text emails by entering necessary details like the sender and recipient email addresses, subject, and message.

## Features
- Send emails via Gmail's SMTP server.
- Securely login using Gmail app passwords.
- Supports plain-text email messages.

## Prerequisites
- **Python 3.x** installed on your machine.
- A Gmail account with **2-Factor Authentication (2FA)** enabled.
- A **Gmail app password** (not your regular Gmail password).

## How to Get a Gmail App Password
To use this script, you **must use a Gmail app password**, not your regular Gmail password. Follow these steps to generate an app password:

1. Enable **2-Factor Authentication** for your Gmail account:  
   [Enable 2FA](https://myaccount.google.com/security-checkup)  
2. After enabling 2FA, go to this link to create a new app password:  
   [Create App Password](https://myaccount.google.com/apppasswords)
3. Use the generated app password when prompted by the script.

## Installation
1. Clone the repository:
   ```bash
   git clone (https://github.com/ibedevesh/GmailAutomation.git)
  

## Usage
 ```bash
python gmail.py
```

## Example Output

1. Enter your Gmail address: example@gmail.com
2. Enter your Gmail password or app password: 
3. Enter the recipient's email address: recipient@example.com
4. Enter the email subject: Hello!
5. Enter the email message: This is a test email.
6. Email sent successfully!


