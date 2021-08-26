import pandas as pd

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'



###LOOKBACK DF FUCTIONS GO HERE
#Takes a lookback distance and pandas dataframe, does least squares polynomial fit. returns poly coefficients and Residuals is sum of squared 
def poly_vars (lb_p,SUB_d_f):
    sub_df = 
    return {x:1234, xx:2421352 ,ssr:3452435}


# takes array of lookback periods 
def poly_vars_to_df ():
    print('90')













if __name__ == '__main__':
    df = pd.read_pickle(f'data/processed/{exchange}/{pair}_{timeframe}.pkl')
    df.info()

def simplify_df (dataframe):
    new_df = dataframe[['Low', 'High', 'Close']].copy()
    return new_df

sim