import os
from flask import Flask, request, jsonify
from arima import arima
from arima import train_arima
from utilities import json_to_csv

app = Flask(__name__)
csv_path = "./tmp/data.csv"
training_data_path = './tmp/training_data.csv'
arima_instance = None


@app.route("/")
def health_check():
    return jsonify({"code": 200, "message": "arima api is up and running"}), 200


@app.route("/forecast", methods=["POST"])
def forecast():
    try:
        request_data = request.get_json(silent=True)
        if request_data:
            try:
                json_to_csv.to_csv(json_object=request_data.get('history'), destination=csv_path)
                forecast_data = arima_instance.forecast(csv_path, request_data.get('historyStartDate'),
                                                        request_data.get('historyEndDate'),
                                                        request_data.get('forecastStartDate'),
                                                        request_data.get('forecastNumberOfWeeks'))
                response = [{"date": a, "unitSold": b} for (a, b) in forecast_data]
                return jsonify(response), 200
            except Exception as e:
                return jsonify({"code": 500, "message": "unable to process history data -> {}".format(e)}), 500
            finally:
                os.remove(csv_path)
        else:
            return jsonify({"code": 400, "message": "bad request"}), 400
    except:
        return jsonify({"code": 500, "message": "unable to get forecast data"}), 500


def create_temp():
    try:
        cwd = os.getcwd()
        os.mkdir("{}/tmp".format(cwd))
    except OSError as err:
        print("Unable to create tmp directory -> {}".format(err))


def initialize_arima():
    try:
        train_arima.fetch_training_set(training_data_path)
        return arima.Arima(data_set_path=training_data_path)
    except Exception as e:
        print('Error while initializing arima {}'.format(e))


if __name__ == "__main__":
    create_temp()
    arima_instance = initialize_arima()
    app.run(port=5000)
