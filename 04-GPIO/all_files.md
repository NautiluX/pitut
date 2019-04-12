# blink.py

```
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    for i in range(21):
        GPIO.output(17, GPIO.LOW)
        time.sleep(1)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
finally:
    GPIO.cleanup()
```

# dht\_print.py

```
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 27

for i in range(10):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("humidity: %s" % humidity)
    print("temperature: %s" % temperature)
    time.sleep(10)
```

# combined.py

```
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

sensor = Adafruit_DHT.DHT11
pin = 27

try:
    for i in range(21):
        GPIO.output(17, GPIO.HIGH)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print("humidity: %s" % humidity)
        print("temperature: %s" % temperature)
        GPIO.output(17, GPIO.LOW)
        time.sleep(10)
finally:
    GPIO.cleanup()
```

# dht\_csv.py

```
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
```

# start.sh

```
#!/bin/bash

./dht_csv.py > data.csv &
./dht_pandas_page.py
```
