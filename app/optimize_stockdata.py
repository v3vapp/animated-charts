# %%
import pandas as pd

# %%
df = pd.read_csv("../data/TSLA_data.csv")
df

# %%
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].astype(int) / 10**9
df

# %%
df.set_index('Date', inplace=True)
df

# %%
df.index.rename(None, inplace=True)
df

# %%
df.columns = df.columns.str.lower()
df


