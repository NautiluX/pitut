#!/usr/bin/env python

from twisted.web import server, resource
from twisted.internet import reactor, task
from twisted.web.static import File
from twisted.web.server import Site

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

values = []

def updateChart():
    try:
        data = pd.read_csv('data.csv', names=["time", "hum", "temp"])
        data.time=pd.to_datetime(data['time'])
        data.set_index(['time'], inplace=True)
        data.plot()
        plt.savefig('dht11_plot.png')
    except:
        pass

l = task.LoopingCall(updateChart)
l.start(10.0)


resource = File('./')
factory = Site(resource)
reactor.listenTCP(8080, factory)

reactor.run()

