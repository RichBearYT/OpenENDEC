#!/usr/bin/python3
# OpenENDEC Driver for "SAGE EAS ENDEC 1822"
#
# Author: Nate Sales (@nwsnate)
# License: GNU General Public License v3.0

import time
import serial

class Endec:
    def __init__(self, callback, port, baud=9600, delay=3):
        self.callback = callback
        self.delay = delay

        # Initialize the serial port
        try:
            self.serial = serial.Serial(port, baud)
        except serial.serialutil.SerialException as e:
            print("[ERROR] Connecting to ENDEC on " + port)
            print(e)
            exit()

        # Make sure the serial port is open
        if not ser.isOpen():
            print("[ERROR] Serial port " + device + " is not open.")
            exit(1)

        self.output = ""

    def monitor(self):
        if self.serial.inWaiting():
            line = self.serial.readline().decode()

            if line.startswith("<ENDECSTART>"):
                self.output = ""

            elif line.startswith("<ENDECEND>"):
                self.callback(output)

            else:
                self.output += line

        else:
            self.output = ""
            time.sleep(self.delay)
