import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import statsmodels.api as sm

def prediction(da):
    df=pd.read_csv("Dateset6.csv")


# In[6]:


    df.head()


# In[7]:


    df.columns=['Date','confirmedtickets']


# In[8]:


    df.head(10)
    df.shape


# In[9]:


    df.tail(10)


# In[10]:

    df['Date']=pd.to_datetime(df['Date'])


# In[11]:


    df.head()


# In[12]:


    df.set_index('Date',inplace=True)


# In[13]:


    df.plot()


# In[14]:


    from statsmodels.tsa.stattools import adfuller


# In[15]:


    result=adfuller(df['confirmedtickets'])


# In[16]:


    def adfuller_test(confirmedtickets):
        result=adfuller(confirmedtickets)
        labels = ['ADF test statistic','p-value','#Lags Used','Number of Observations Used']
        for value,label in zip(result,labels):
            print(label+" = "+str(value))
        if result[1] <= 0.05:
            print("stationary")
        else:
            print("Non stationary")


# In[17]:


    adfuller_test(df['confirmedtickets'])


# In[18]:


    from statsmodels.graphics.tsaplots import plot_acf,plot_pacf


# In[19]:


    fig=plt.figure(figsize=(12,8))
    ax1=fig.add_subplot(211)
    fig=sm.graphics.tsa.plot_acf(df['confirmedtickets'].iloc[0:],lags=40,ax=ax1)
    ax2=fig.add_subplot(212)
    fig=sm.graphics.tsa.plot_pacf(df['confirmedtickets'].iloc[0:],lags=40,ax=ax2)


# In[20]:


#p=1,q=1,2,d=0
    import warnings
    from statsmodels.tsa.arima_model import ARIMA


# In[21]:


    model=ARIMA(df['confirmedtickets'],order=(1,0,1))
    model_fit=model.fit()


# In[22]:


    model_fit.summary()


# In[23]:


    df['forecast']=model_fit.predict(start=90,end=103,dynamic=True)
    df[['confirmedtickets','forecast']].plot(figsize=(12,8))


# In[24]:


    from pandas.plotting import autocorrelation_plot


# In[25]:


    df.tail()
# In[26]:


    model=sm.tsa.statespace.SARIMAX(df['confirmedtickets'],order=(1,0,2),seasonal_order=(1,1,1,12))
    results=model.fit()


# In[27]:


    df['forecast']=results.predict(start=90,end=103,dynamic=True)
    df[['confirmedtickets','forecast']].plot(figsize=(12,8))


# In[28]:


    df.tail()


# In[29]:


    from pandas.tseries.offsets import DateOffset
#


# In[30]:


    future_dates=[df.index[-1]+DateOffset(days=x)for x in range(0,364)]


# In[31]:


    future_dataset_df=pd.DataFrame(index=future_dates[0:],columns=df.columns)


# In[32]:


    future_dataset_df.tail()


# In[33]:


    future_df=pd.concat([df,future_dataset_df])


# In[34]:


    future_df['forecast']=results.predict(start=300,end=394,dynamic=True)


# In[35]:


    future_df[['confirmedtickets','forecast']].plot(figsize=(12,8))


# In[38]:


   # print(df)


# In[61]:


#print(df.loc[df['Date'] == '2019-10-22']['forecast'])


# In[60]:


#df.loc[df["Date"] == "2019-10-22", "forecast"]


# In[46]:


   # df.loc['2019-10-22','forecast']


# In[56]:


    #xdate='2021-5-22'
    xdate=da


# In[58]:


    y=future_df.loc[xdate,'forecast']


# In[59]:


    return y
#prediction(da='2021-5-22') 








