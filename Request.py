#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import requests
import time

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # Print UID
    	clothes_uid = "-".join("{0}".format(s) for s in uid)
        clothes_url = "http://192.168.2.1:3000/clothes/{0}".format(clothes_uid)
        requests.get(clothes_url)
        print clothes_url
        time.sleep(2)