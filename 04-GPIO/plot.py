import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


while True:
    data = pd.read_csv('data.csv', names=["time", "hum", "temp"])
    data.time=pd.to_datetime(data['time'])
    data.set_index(['time'], inplace=True)
    data.plot()
    plt.savefig('dht11_plot.png')
