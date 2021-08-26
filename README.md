https://www.machinelearningplus.com/time-series/time-series-analysis-python/


Channel breakout bot. 
Continuously is looking for a tight long channel. When it detects a good channel it trades the breakout. 
Do this asymmetrically. Markets will behave differently on the way down then up because of human bias. 

Variables:
- lookback period
- absolute variance from the linear regression
- entry threshold
- exit threshold
- stop_loss_thsh

Steps:
1) get close data
2) see lin reg chanel
3) optimise for variables in backtest
4) test on test data
5) put into a production environment. 

Data splits:
Train 2018-01-01 to 2020-12-31
Valiation BACKTEST
Test 2021-01-01 to 2021-07-31