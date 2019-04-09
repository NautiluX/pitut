import Adafruit_DHT, time, json, datetime

from twisted.web import server, resource
from twisted.internet import reactor, task


sensor = Adafruit_DHT.DHT11
pin = 4

values = []

def updateHumidity():
    global values
    newValue = {
        "humidity": 42,
        "temperature": 42,
        "date": datetime.datetime.now().isoformat()
        }
    newValue["humidity"], newValue["temperature"] = Adafruit_DHT.read_retry(sensor, pin)
    print("updated humidity: {}, temp: {}".format(newValue["humidity"], newValue["temperature"]))
    values.append(newValue)

l = task.LoopingCall(updateHumidity)
l.start(10.0)

class MyServer(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return """
        <script>
        window.onload = function () {
                realdata="""+json.dumps(values)+""";
                    data = [{
                                type: "area",
                                        dataPoints: realdata.map((v)=>{
                                                        return {
                                                                            x: new Date(v.date),
                                                                                            y: v.humidity
                                                                                                        };
                                                                })
                                            },{
                                                        type: "area",
                                                                dataPoints: realdata.map((v)=>{
                                                                                return {
                                                                                                    x: new Date(v.date),
                                                                                                                    y: v.temperature
                                                                                                                                };
                                                                                        })
                                                                    }];
                                                var chart = new CanvasJS.Chart("chartContainer", {
                                                            animationEnabled: true,
                                                                    title: {
                                                                                    text: "Raspberry Pi Measured hum/temp"
                                                                                            },
                                                                            axisX: {
                                                                                            includeZero: true,
                                                                                                        title: "date"
                                                                                                                },
                                                                                    axisY: {
                                                                                                    includeZero: true,
                                                                                                                title: "temperature/humidity"
                                                                                                                        },
                                                                                            data: data
                                                                                                });
                                                chart.render();
                                                }
        </script>

        <div id="chartContainer" style="height: 370px; width: 100%;"></div>
        <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
        """

s = server.Site(MyServer())
reactor.listenTCP(8080, s)
reactor.run()

