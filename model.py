import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import statsmodels.api as sm

 df=pd.read_csv("DataSET.csv")
 df.columns=['Date','confirmedtickets']
 df['Date']=pd.to_datetime(df['Date'])
 df.set_index('Date',inplace=True)
 df.plot()
 from statsmodels.tsa.stattools import adfuller
 def adfuller_test(confirmedtickets):
    result=adfuller(confirmedtickets)
    labels = ['ADF test statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+" = "+str(value))
    if result[1] <= 0.05:
        print("stationary")
    else:
        print("Non stationary")
 adfuller_test(df['confirmedtickets'])
 from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
 fig=plt.figure(figsize=(12,8))
 ax1=fig.add_subplot(211)
 fig=sm.graphics.tsa.plot_acf(df['confirmedtickets'].iloc[0:],lags=40,ax=ax1)
 ax2=fig.add_subplot(212)
 fig=sm.graphics.tsa.plot_pacf(df['confirmedtickets'].iloc[0:],lags=40,ax=ax2)  
 import warnings
 from statsmodels.tsa.arima_model import ARIMA   
 model=ARIMA(df['confirmedtickets'],order=(1,0,1))
 model_fit=model.fit()   
 model_fit.summary()
 df['forecast']=model_fit.predict(start=90,end=103,dynamic=True)
 df[['confirmedtickets','forecast']].plot(figsize=(12,8))
 from pandas.plotting import autocorrelation_plot
 model=sm.tsa.statespace.SARIMAX(df['confirmedtickets'],order=(1,0,2),seasonal_order=(1,1,1,12))
 results=model.fit()
 df['forecast']=results.predict(start=90,end=103,dynamic=True)
 df[['confirmedtickets','forecast']].plot(figsize=(12,8))
 from pandas.tseries.offsets import DateOffset
 future_dates=[df.index[-1]+DateOffset(days=x)for x in range(0,103)]