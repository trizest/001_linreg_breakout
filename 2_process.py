import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'
oclhvColumns = ['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']
lookback_period = [5,10,20,50,100,200,500,1000,2000]
#variance_factor this gets put in the df and looked for along with the polynomials. 
entry_thrsh = 1.05
exit_thrsh = 1.10
stoploss_thrsh = 1.05

###WHOLE OF DF FUNCTIONS GO HERE. 
#takes the csv, sets index with datetimeformat, returns a pandas dataframe
def read_csv(ex, p, tf):
    d_f = pd.read_csv(f'data/1_fresh/{ex}/{p}_{tf}.csv', names=oclhvColumns)
    d_f['Date'] = pd.to_datetime(d_f['Unix'], unit='ms')
    d_f = d_f.set_index('Date')
    d_f = d_f[['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']]
    return d_f

#returns only the columns you want to use in a pandas dataframe
def simplify_df (d_f):
    new_df = d_f[['Close']].copy()
    return new_df


#puts the data in the jar
def pickle_df(ex, p, tf, d_f):
    path = Path("./data/2_processed/", str(ex))
    path.mkdir(parents=True, exist_ok=True)
    full_path = path / str(f'{p}_{tf}.pkl')
    d_f.to_pickle(full_path)
    print(full_path)

if __name__ == '__main__':
    df = read_csv(exchange, pair, timeframe)
    df = simplify_df (df)
    pickle_df(exchange, pair, timeframe, df)
    

    df.info()
    print(df.head(10))