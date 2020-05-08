# config.py
# OpenENDEC Configuration loader
# Author: Nate Sales (@nwsnate)

import yaml
import constants

with open("config.yml") as config_file:
    data = yaml.safe_loads(config_file, Loader=yaml.FullLoader)

    # Begin ENDEC configuration

    try:
        model = data["endec"]["model"]
    except KeyError:
        print("ERROR: ENDEC model not found.")
        exit()
    else:
        if model not in constants.ENDEC_MODELS:
            print("ERROR: ENDEC model not supported.")

    try:
        port = data["endec"]["port"]
    except KeyError:
        print("ERROR: ENDEC port not found.")
        exit()

    try:
        baud = int(data["endec"]["baud"])
    except KeyError:
        baud = 9600 # Default to 9600 baud

    print("Using " + model + " on " + port + " at " + str(baud) + " baud")

    # End ENDEC configuration

    # Begin output configuration

    # Begin email output configuration
    try:
        email = data["outputs"]["email"]
    except KeyError:
        pass # No email configuration
    else:
        try:
            email_username = email["username"]
            email_password = email["password"]
            email_server = email["server"]
            email_port = int(email["port"])
            email_recepients = list(email["recepients"])
        except KeyError:
            print("ERROR: Email configuration is wrong. Check the example config.yml for how this should look.")
        else:
            email_output = True
            print("Using " + email_username + " on server " + email_server + ":" + str(email_port))
            for recepient in email_recepients:
                print(" - " + recepient)
    # End email output configuration

    # Begin discord configuration
    try:
        discord = data["outputs"]["discord"]
    except KeyError:
        pass # No email configuration
    else:
        try:
            discord_webhook = discord["webhook"]
        except KeyError:
            print("ERROR: Discord webhook not found.")
            exit()
        else:
            discord_output = True
            print("Using Discord webhook: " + discord_webhook)
    # End discord configuration

    # End output configuration

    if (not email_output) and (not discord_output):
        print("ERROR: No outputs configured. You must enable at least one output method.")
        exit()
    else:
        print("OpenENDEC configuration complete.")
