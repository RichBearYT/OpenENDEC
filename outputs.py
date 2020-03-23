# OpenENDEC Output Sources

import requests
import smtplib

# Email config
username = ""
password = ""
server = ""
port = ""
sender = username
recepients = []

# Discord config
webhook = ""


def alert_email(message):
    server = smtplib.SMTP(server, port)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recepients, "\r\n".join(["To: %s" % sender, "From: %s" % sender, "Subject: %s" % "EAS Alert", "", message]))
    server.quit()

def alert_discord(message):
    requests.post(webhook, data={"content": message})
