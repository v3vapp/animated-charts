import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation

# load data
data = pd.read_csv("data/TSLA_data.csv")
data['Date'] = pd.to_datetime(data['Date'])
data = data.set_index('Date')

# plot the candlestick chart
fig, ax = plt.subplots()

def update(num):
    ax.clear()
    start = data.index[-48 + num]
    end = data.index[-48 + num + 1]
    data_ = data[start:end]
    candlestick_ohlc(ax, zip(mdates.date2num(data_.index.to_pydatetime()),
                            data_['Open'], data_['High'],
                            data_['Low'], data_['Close']),
                    width=0.6, colorup='g', colordown='r')
    ax.xaxis_date()

ani = FuncAnimation(fig, update, frames=48, interval=10000)
plt.show()