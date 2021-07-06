import pandas as pd

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'

if __name__ == '__main__':
    df = pd.read_pickle(f'data/processed/{exchange}/{pair}_{timeframe}.pkl')
    df.info()

def simplify_df (dataframe):
    new_df = dataframe[['Low', 'High', 'Close']].copy()
    return new_df

sim