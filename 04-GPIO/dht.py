import Adafruit_DHT, time

from twisted.web import server, resource
from twisted.internet import reactor, task


sensor = Adafruit_DHT.DHT11
pin = 4

humidity = 0
temperature = 0

def updateHumidity():
    global humidity
    global temperature
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("updated humidity: {}, temp: {}".format(humidity, temperature))

l = task.LoopingCall(updateHumidity)
l.start(3.0)

class MyServer(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
	return "humidity: {} temp: {}".format(humidity, temperature)

s = server.Site(MyServer())
reactor.listenTCP(8080, s)
reactor.run()
