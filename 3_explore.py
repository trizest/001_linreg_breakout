import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('data/processed/Binance/btc_usdt_15m.pkl')
df.info()

print(df['Close'].plot())
