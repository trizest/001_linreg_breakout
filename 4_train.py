import pandas as pd
import numpy as np

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'
id = 'train'

lookback_period = [5,10,20,50,100,200,500,1000,2000]
#variance_factor this gets put in the df and looked for along with the polynomials. 
entry_thrsh = 1.05
exit_thrsh = 1.10
stoploss_thrsh = 1.05


###LOOKBACK DF FUCTIONS GO HERE
def rolling_polyfit(df_col, lb_p,deg):
    coef_x1 = df_col.rolling(lb_p).apply(lambda y: np.polyfit(range(len(y)), y, deg)[0])
    coef_x0 = df_col.rolling(lb_p).apply(lambda y: np.polyfit(range(len(y)), y, deg)[1])   
    coefs = [coef_x1, coef_x0]
    # yfit = close_vals.rolling(lb_p).apply(lambda y: np.polyval(coefs,range(len(y))))
    # residual = np.sum((breadths-yfit)**2)
    return coefs




def sum_of_squares():
    return print('placeholder')



if __name__ == '__main__':
    df = pd.read_pickle(f'data/2_processed/{exchange}/{pair}_{timeframe}_{id}.pkl')
    df.info()

    df['coef_x1'] = rolling_polyfit(df['Close'],lookback_period[0],1)[0]
    df['coef_x0'] = rolling_polyfit(df['Close'],lookback_period[0],1)[1]

    print(df.head(5))
    print(df.tail(5))