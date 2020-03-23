#!/usr/bin/python3
# OpenENDEC v1.9.0

from drivers.sage.endec1822 import Endec
import config
import outputs

if config.email_output:
    outputs.username = config.email_username
    outputs.password = config.email_password
    outputs.server = config.email_server
    outputs.port = config.email_port
    outputs.recepients = config.email_recepients
if config.discord_output:
    outputs.discord_webhook = config.discord_webhook

def endec_callback(data):
    if config.email_output:
        outputs.alert_email(data)

    if config.discord_output:
        outputs.alert_discord(data)

endec = Endec(endec_callback, "/dev/ttyACM0")

while True:
    endec.monitor()
