import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
import seaborn as sns
import pandas as pd

# 株価の時系列データの読み込み
df = pd.read_csv("data/TSLA_data.csv")

# フレームごとの処理
def update(frame):
    plt.clf()
    sns.lineplot(x='Date', y='Close', data=df[df['Date'] <= df['Date'].iloc[frame]])
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.title("Stock Price Over Time")

# アニメーションの作成
ani = animation.FuncAnimation(plt.gcf(), update, frames=len(df), interval=100)

plt.show()

