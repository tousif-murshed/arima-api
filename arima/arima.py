import pandas as pd
from pmdarima import auto_arima


class Arima:

    def __init__(self, data_set_path):
        data_set = pd.read_csv(data_set_path, index_col=0)
        data_set.index = pd.to_datetime(data_set.index)
        self.model = auto_arima(data_set, start_p=0, start_q=0, max_p=3, max_q=3, m=7, start_P=0, seasonal=True,
                                d=0, D=0, trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)
        print('Arima successfully initialized')

    def forecast(self, history_data_path, history_start_date, history_end_date, forecast_start_date,
                 forecast_number_of_weeks):
        try:
            history_data = pd.read_csv(history_data_path, index_col=0, usecols=['date', 'unitSold'])
            history_data.index = pd.to_datetime(history_data.index)
            training_model = history_data.loc[history_start_date:history_end_date]
            self.model.fit(training_model)
            number_of_days = int(forecast_number_of_weeks) * 7
            forecast_data = [int(fct) for fct in self.model.predict(number_of_days)]
            forecast_date_range = [date.strftime('%Y-%m-%d') for date in
                                   pd.date_range(start=forecast_start_date, periods=number_of_days)]
            return zip(forecast_date_range, forecast_data)
        except Exception as e:
            print("Error while forecasting -> {}".format(e))
            return []
