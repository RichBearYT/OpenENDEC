#!/usr/bin/python3
# openendec.py
#
# OpenENDEC
# License: GNU General Public License v3.0


import time
import serial
import traceback
import requests

device = "COM1"
webhook = "webhook url goes here"
delay = 2.5

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
        time.sleep(delay)
