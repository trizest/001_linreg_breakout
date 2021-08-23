import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'
oclhvColumns = ['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']
lookback_period = [5,10,20,50,100,200,500,1000,2000]
#variance_factor this gets put in the df and looked for along with the polynomials. 
entry_thrsh = 1.05
exit_thrsh = 1.10
stoploss_thrsh = 1.05


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

#Takes a lookback distance and pandas dataframe, does least squares polynomial fit. returns poly coefficients and Residuals is sum of squared 
def poly_vars (lb_p,d_f):
    
    return {x:1234, xx:2421352 ,ssr:3452435}


# takes array of lookback periods 
def poly_vars_to_df ():
    print('90')


#puts the data in the jar
def pickle_df(ex, p, tf, d_f):
    d_f.to_pickle(f'data/processed/{ex}/{p}_{tf}.pkl')
    print(f'data/processed/{ex}/{p}_{tf}.pkl')


if __name__ == '__main__':
    df = read_csv(exchange, pair, timeframe)
    df = simplify_df (df)
    pickle_df(exchange, pair, timeframe, df)

    df.info()
    print(df.head(10))