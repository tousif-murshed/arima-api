import pandas as pd
from pmdarima import auto_arima


# data = pd.read_csv('dataPhSales.csv', index_col=0)
# data.index = pd.to_datetime(data.index)
# print(data.head())
#
# stepwise_model = auto_arima(data, start_p=0, start_q=0,
#                             max_p=3, max_q=3, m=7,
#                             start_P=0, seasonal=True,
#                             d=0, D=0, trace=True,
#                             error_action='ignore',
#                             suppress_warnings=True,
#                             stepwise=True)
# print(stepwise_model.aic())
#
# train = data.loc['2019-01-01':'2019-11-07']
# test = data.loc['2019-11-08':]
# stepwise_model.fit(train)
# future_forecast = stepwise_model.predict(n_periods=31)
# print(future_forecast)


class Arima:
    start_p = 0
    start_q = 0
    max_p = 3
    max_q = 3
    m = 7
    start_P = 0
    seasonal = True
    d = 0
    D = 0
    trace = True
    error_action = 'ignore'
    suppress_warnings = True
    stepwise = True

    def __init__(self, data_set_path):
        data_set = pd.read_csv(data_set_path, index_col=0, usecols=['date', 'unitSold'])
        data_set.index = pd.to_datetime(data_set.index)
        data_set.to_csv('./tmp/test.csv')
        self.model = auto_arima(data_set, self.start_p, self.start_q, self.max_p, self.max_q, self.m, self.start_P,
                                self.seasonal, self.d, self.D, self.trace, self.error_action, self.suppress_warnings,
                                self.stepwise)
        print('Arima successfully initialized')

    def forecast(self, history_data, history_start_date, history_end_date, forecast_start_date,
                 forecast_number_of_weeks):
        try:
            training_model = history_data.loc[history_start_date:history_end_date]
            self.model.fit(training_model)
            forecast_data = self.model.predict(forecast_number_of_weeks)
            number_of_days = forecast_number_of_weeks * 7
            forecast_date_range = pd.date_range(start=forecast_start_date, periods=number_of_days)
            return zip(forecast_date_range, forecast_data)
        except Exception as e:
            print("Error while forcasting -> {}".format(e))
            return []
