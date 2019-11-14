from flask import Flask, request, jsonify
from utilities import json_to_csv
from utilities import csv_to_json
import os
from arima import train_arima
from arima import arima

app = Flask(__name__)
csv_path = "./tmp/data.csv"
training_data_path = './tmp/training_data.csv'


@app.route("/")
def health_check():
    return jsonify({"code": 200, "message": "arima api is up and running"}), 200


@app.route("/forecast", methods=["POST"])
def forecast():
    try:
        request_data = request.get_json(silent=True)
        if request_data:
            try:
                json_to_csv.to_csv(json_object=request_data, destination=csv_path)
                data = csv_to_json.to_json(csv_path)
                return data, 200
            except:
                return jsonify({"code": 500, "message": "unable to process history data"}), 500
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
        arima.Arima(data_set_path=training_data_path)
    except Exception as e:
        print('Error while initializing arima {}'.format(e))


if __name__ == "__main__":
    create_temp()
    initialize_arima()
    app.run(port=5000)
