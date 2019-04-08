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
