# OpenENDEC
Open source digital ENDEC Emergency Alert System controller. OpenENDEC is an integrated EAS controller and relay interface for use with commertial ENDECs or open source DIY hardware controllers like the Arduino.



#### Compatability
OpenENDEC officially supports the SAGE EAS ENDEC "News Feed" output format. This is a shared standard, so other ENDECs supporting "News Feed" will likely work too.



#### Software Setup

Configuration for OpenENDEC is found in the `config.yml` file. Set up your serial port, baud rate, and output settings, and you're good to go!

Running `openendec.py` will read the config and start monitoring for alerts.

It's best to also configure a service on your host machine to start at boot.



#### Hardware Setup

Written by Evan Vander Stoep

First we want to set the device output type on the ENDEC.

From the front panel, go to:

`MENU > DEVICES > COM2 > DEVICE TYPE > NEWSFEED` and press enter, then enter the admin passcode.

You may select any COM port for use with OpenENDEC.

---

Then set the Baud Rate by going to:

`MENU > DEVICES > COM2 > DEVICE TYPE > BAUD RATE > 9600` and press enter, then enter the admin passcode.

Again, substituting COM2 with the COM port that your OpenENDEC computer is connected to.

Now the ENDEC is setup!

---------------
You need to make a cable that goes to the COM Port that you chose, to the PC's serial input.

(NOTE: If you don't have a serial port on your computer, you can buy an "RS-232 to US" adapter.)

The cable is a standard NULL MODEM CABLE.
Each side of the cable is a male DB-9 connector.
Pins 2 & 3 are swapped from each end of the cable. (TX/RX)

DB9 Pinout
 1 - 1
 2 - 3
 3 - 2
 4 - 4
 5 - 5
 6 - 6
 7 - 7
 8 - 8

NOTE: Leave pin 9 disconnected, it is accessory power that could fry the PC COM port.



#### License

GNU GPLv3!



#### Contributors

[Nate Sales](htps://github.com/natesales) for software development of drivers, outputs, linking and interop testing.

[Emma Hones](https://github.com/kernelpanic3) for the original News Feed to webhook script.

[Evan Vander Stoep](https://github.com/EvanVS) for hardware support and development, documentation, and testing.