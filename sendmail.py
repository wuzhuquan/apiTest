import smtplib
import basedata
from email.mime.text import MIMEText
# 发送通知邮件
def sendMail(text):
    sender = basedata.MAIL_SENDER
    receiver = basedata.MAIL_RECEIVER
    subject = basedata.MAIL_TITLE
    smtpserver = basedata.SMTP_SERVER
    username = basedata.MAIL_USERNAME
    password = basedata.MAIL_PASSWOED

    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()