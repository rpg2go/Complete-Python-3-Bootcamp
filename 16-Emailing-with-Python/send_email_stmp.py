import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()

smtp_object.starttls()

email = getpass.getpass("What is your email address ? ")
pwd   = getpass.getpass("What is your password ? ")

smtp_object.login(email, pwd)

from_address = "test@python.com"
to_address = "druga.marius@gmail.com"

subject = input("Enter your subject line: ")
message = input("Enter your message:" )

msg = "Subject: " + subject + "\n" + message

print("Sending email....")
smtp_object.sendmail(from_address, to_address, msg)
print("Email sent!")


smtp_object.quit()