
import pandas as pd
from finta import TA

test = 1
hello = 0

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'
oclhvColumns = ['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']



def read_csv(ex, p, tf):
    d_f = pd.read_csv(f'data/fresh/{ex}/{p}_{tf}.csv', names=oclhvColumns)
    d_f['Date'] = pd.to_datetime(d_f['Unix'], unit='ms')
    d_f = d_f.set_index('Date')
    d_f = d_f[['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']]
    return d_f


def add_tech_ind(dataframe):
    dataframe['SMA12'] = TA.SMA(dataframe, 12)
    dataframe['SMA21'] = TA.SMA(dataframe, 21)
    dataframe['SMA55'] = TA.SMA(dataframe, 55)
    dataframe['SMA100'] = TA.SMA(dataframe, 100)
    dataframe['RSI'] = TA.RSI(dataframe)
    dataframe['OBV'] = TA.OBV(dataframe)
    return dataframe

def simplify_df (dataframe):
    new_df = dataframe[['Low', 'High', 'Close']].copy()
    return new_df

def pickle_df(ex, p, tf, d_f):
    # IT WENT IN THE JAR HERE!!
    d_f.to_pickle(f'data/processed/{ex}/{p}_{tf}.pkl')
    print(f'data/processed/{ex}/{p}_{tf}.pkl')


if __name__ == '__main__':
    df = read_csv(exchange, pair, timeframe)
    df = simplify_df (df)
    pickle_df(exchange, pair, timeframe, df)

    df.info()
    print(df.head(1))
