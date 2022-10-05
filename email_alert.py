import pywhatkit
import datetime
"""import smtplib
from email.message import EmailMessage


def email_alert(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "hackathon959@gmail.com"
    msg['form'] = user
    password = "hqiifuovcdattbhp"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
   server.send_message(msg)

    server.quit()
email_alert("vrajparikh0312@gmail.com", "Alert", "An Unknown person is detected!!!!!!")"""
current_time = datetime.datetime.now()
mint = current_time.minute + 1
hour = current_time.hour
pywhatkit.sendwhatmsg('+917778873777', 'Hey free msg', hour, mint)

print(current_time.hour)
print(current_time.minute)