from flask import Flask, request, jsonify
from utilities import json_to_csv
import os

app = Flask(__name__)
csv_path = "./tmp/data.csv"


@app.route("/")
def health_check():
    return jsonify({"code": 200, "message": "arima api is up and running"}), 200


@app.route("/forecast", methods=["POST"])
async def forecast():
    try:
        request_data = request.get_json()
        if request_data:
            await json_to_csv.to_csv(json_object=request_data, destination=csv_path)
            return jsonify({"code": 200, "message": "successfully processed incoming request"}), 200
        else:
            return jsonify({"code": 400, "message": "bad request"}), 400
    except:
        return jsonify({"code": 500, "message": "unable to get forecast data"}), 500
    finally:
        os.remove(csv_path)


app.run(port=5000)
