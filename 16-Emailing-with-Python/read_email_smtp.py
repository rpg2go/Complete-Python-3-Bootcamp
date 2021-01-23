import imaplib
import getpass
import email

smtp_server = imaplib.IMAP4_SSL('imap.gmail.com')

mail = getpass.getpass("What is your email address ? ")
pwd  = getpass.getpass("What is your password ? ")

print("Connecting to smtp_server..")
smtp_server.login(mail, pwd)
print("Connected!")

print(smtp_server.list())

smtp_server.select('inbox')

#typ, date = smtp_server.search(None, 'ON 23 January 2021')
typ, data = smtp_server.search(None, 'SUBJECT "Python test"')
print(typ, data)

email_id = data[0]
result, email_data = smtp_server.fetch(email_id, '(RFC822)')

#email data
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
