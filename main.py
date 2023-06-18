import smtplib
from config import email_pas, my_email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

server.ehlo()

server.login(my_email, email_pas)

msg = MIMEMultipart()
# msg["From"] = "Дмитрий Нижников"
msg["Subject"] = "Свободная вакансия"

with open("back_declined_mes.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

mail_list = []
with open("mail_list.txt", "r") as ml:
    for line in ml.readlines():
        line = line.strip("\n")
        mail_list.append(line)

for mail in mail_list:
    msg["To"] = mail
    text = msg.as_string()

    server.sendmail(my_email, mail, text)
