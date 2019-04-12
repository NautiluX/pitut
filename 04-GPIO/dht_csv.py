#!/usr/bin/env python

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import datetime
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

sensor = Adafruit_DHT.DHT11
pin = 27

try:
    for i in range(21):
        GPIO.output(17, GPIO.HIGH)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        now = datetime.datetime.now()
        now_iso = now.isoformat()
        print("%s,%s,%s" % (now_iso, humidity, temperature))
        sys.stdout.flush()
        GPIO.output(17, GPIO.LOW)
        time.sleep(10)
finally:
    GPIO.cleanup()
