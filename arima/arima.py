import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as ply
from chart_studio.plotly import plot_mpl
from statsmodels.tsa.seasonal import seasonal_decompose
import cufflinks as cf
from pmdarima import auto_arima

data = pd.read_csv('dataPhSales.csv', index_col=0)
data.index = pd.to_datetime(data.index)
print(data.head())

stepwise_model = auto_arima(data, start_p=0, start_q=0,
                           max_p=3, max_q=3, m=7,
                           start_P=0, seasonal=True,
                           d=0, D=0, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())

train = data.loc['2019-01-01':'2019-11-07']
test = data.loc['2019-11-08':]
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=31)
print(future_forecast)

# future_forecast = pd.DataFrame(future_forecast,index = test.index,columns=['Prediction'])
# pd.concat([test,future_forecast],axis=1).iplot()

