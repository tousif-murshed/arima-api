from flask import Flask, request, jsonify
from utilities import json_to_csv
from utilities import csv_to_json
import os
from os import environ

app = Flask(__name__)
csv_path = "./tmp/data.csv"


@app.before_first_request
def create_temp():
    print("The environment variable value is {}".format(environ["TEST"]))
    try:
        cwd = os.getcwd()
        os.mkdir("{}/tmp".format(cwd))
    except OSError as err:
        print("Unable to create tmp directory -> {}".format(err))


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


if __name__ == "__main__":
    app.run(port=5000)
