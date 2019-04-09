import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 27

for i in range(10):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("humidity: %s" % humidity)
    print("temperature: %s" % temperature)
    time.sleep(10)
