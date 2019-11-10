import pandas as pd
from pmdarima import auto_arima
data = pd.read_csv("PyArima//data2.csv", index_col=0)

data.index = pd.to_datetime(data.index)
data.columns = ['Sales']
print(data.head())
stepwise_model = auto_arima(data, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',
                           suppress_warnings=True,
                           stepwise=True)
print(stepwise_model.aic())
train = data.loc['1985-01-01':'2016-12-01']
test = data.loc['2017-01-01':]
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=5)
print(future_forecast)




# async def forecast():
#
#
