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
train_start = "2018-01-01 00:00:00"
train_finish = "2020-12-31 23:45:00"
test_start = "2021-01-01 00:00:00"
test_finish = "2021-06-30 00:00:00"


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
def pickle_df(ex, p, tf, d_f,id):
    path = Path("./data/2_processed/", str(ex))
    path.mkdir(parents=True, exist_ok=True)
    full_path = path / str(f'{p}_{tf}_{id}.pkl')
    d_f.to_pickle(full_path)
    print(full_path)

#this fuction made redundand by simply putting the 
def train_set(d_f):
    df_x = d_f[train_start:train_finish] 
    return df_x

#run. saves two processed df's in pickles. 
if __name__ == '__main__':
    df = read_csv(exchange, pair, timeframe)
    df = simplify_df (df)
    train_df = df[train_start:train_finish]
    pickle_df(exchange, pair, timeframe, train_df, "train")
    test_df = df[test_start:test_finish]
    pickle_df(exchange, pair, timeframe, test_df, "test")

    train_df.info()
    print(train_df.head(10))
    print(test_df.tail(10))

