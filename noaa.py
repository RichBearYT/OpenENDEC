import requests
import feedparser
import smtplib
import time
import serial
import gtts
import os
from subprocess import Popen, PIPE, STDOUT

def speak(text):
    os.system("gtts-cli " + text + "' --output output.mp3")
    os.system("mpg123 -w output.wav output.mp3")
    ser.write("KEY\n".encode())
    time.sleep(1.5)
    os.system("aplay -D plughw:CARD=Device,DEV=0 output.wav")
    ser.write("UNKEY\n".encode())

print("Initializing serial port...", end="", flush=True)
ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)

while not ser.isOpen(): # Wait for serial port to open
    time.sleep(0.25)

ser.flushInput()  # Flush input and output to ensure
ser.flushOutput() # there isn't anything in the buffer
print("DONE")

p = Popen("sudo rtl_fm -f " + config.FREQUENCY + "M -s 22050 -g 50 | multimon-ng -a DTMF -", stdout=PIPE, stderr=STDOUT, shell=True)
while True:
    line = p.stdout.readline()
    if not line:
        print("Breaking.")
        break

    line = line.decode().strip()
    if line.startswith("DTMF"):
        chr = line.strip("DTMF: ")

        if (chr == "1"):
            speak("This is a test of the OpenENDEC remote station.")

        elif (chr == "2"):
            feed = feedparser.parse("https://alerts.weather.gov/cap/or.php?x=0")

            for entry in feed["items"]:
                title = entry["title"]
                summary = entry["summary"]

                # Time data
                published = entry["published"]
                updated = entry["updated"]
                effective = entry["cap_effective"]
                expires = entry["cap_expires"]

                # CAP Data
                event = entry["cap_event"]
                urgency = entry["cap_urgency"]
                severity = entry["cap_severity"]
                certainty = entry["cap_certainty"]
                area = entry["cap_areadesc"]

                value = entry["value"]

                raw = title + "\n"
                for x in summary.split(" * "):
                    raw += x + "\n"
                raw += value

                mini = event + "\n"
                mini += "Effective " + effective + "\n"
                mini += "Urgency: " + urgency + "\n"
                mini += "Severity: " + severity + "\n"
                mini += "Certainty: " + certainty + "\n"
                mini += "Area: " + area


                server = smtplib.SMTP(config.SERVER, config.PORT)
                server.ehlo()
                server.starttls()
                server.login(config.USERNAME, config.PASSWORD)
                server.sendmail(config.USERNAME, config.RECEPIENTS, "\r\n".join(["To: %s" % config.FROM, "From: %s" % config.FROM, "Subject: %s" % "", "", raw]))
                server.quit()

                requests.post(config.WEBHOOK, data={"content": "```" + raw + "```"})
