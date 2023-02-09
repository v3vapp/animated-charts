import finplot as fplt
import numpy as np
import pandas as pd


FPS = 30
anim_counter = 0
spots = None
labels_plot = None


def gen_spots(ax, df):
    global spots
    spot_ser = df['low'] - 0.1
    spot_ser[(spot_ser.reset_index(drop=True).index - anim_counter) % 20 != 0] = np.nan
    if spots is None:
        spots = spot_ser.plot(kind='scatter', color=2, width=2, ax=ax, zoomscale=False)
    else:
        spots.update_data(spot_ser)


def gen_labels(ax, df):
    global labels_plot
    y_ser = df['volume'] - 0.1
    y_ser[(y_ser.reset_index(drop=True).index + anim_counter) % 50 != 0] = np.nan
    dft = y_ser.to_frame()
    dft.columns = ['y']
    dft['text'] = dft['y'].apply(lambda v: str(round(v, 1)) if v>0 else '')
    if labels_plot is None:
        labels_plot = dft.plot(kind='labels', ax=ax)
    else:
        labels_plot.update_data(dft)


def move_view(ax, df):
    global anim_counter
    x = -np.cos(anim_counter/100)*(len(df)/2-50) + len(df)/2
    w = np.sin(anim_counter/100)**4*50 + 50
    fplt.set_x_pos(df.index[int(x-w)], df.index[int(x+w)], ax=ax)
    anim_counter += 1


def animate(ax, ax2, df):
    gen_spots(ax, df)
    gen_labels(ax2, df)
    move_view(ax, df)


df = pd.read_csv("data/TSLA_data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].astype(int) / 10**9
df.set_index('Date', inplace=True)
df.index.rename(None, inplace=True)
df.columns = df.columns.str.lower()

# print(df)

ax,ax2 = fplt.create_plot('Things move', rows=2, init_zoom_periods=100, maximize=False)
df.plot(kind='candle', ax=ax)
df[['open','close','volume']].plot(kind='volume', ax=ax2)
fplt.timer_callback(lambda: animate(ax, ax2, df), 1/FPS)
fplt.show()