#!/usr/bin/python3
# endec.py
#
# OpenENDEC
# License: GNU General Public License v3.0

import time
import serial
import requests

device = "COM1"
webhook = "webhook url goes here"

# Initialize the serial device
ser = serial.Serial(device, 9600)

# Make sure the serial device is open
if not ser.isOpen():
    print("[ERROR] Serial port " + device + " is not open.")
    exit(1)

output = ""
while True:
    if ser.inWaiting():
        line = ser.readline().decode()

        if line.startswith("<ENDECSTART>"):
            output = ""

        elif line.startswith("<ENDECEND>"):
            requests.post(webhook, data={"content": output})

        else:
            output += line + "\n"

    else:
        output = ""
        time.sleep(3)
