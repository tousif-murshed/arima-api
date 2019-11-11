import csv
import json
import pandas as pd


def to_json_file(csv_file_path="", destination=""):
    try:
        with open(csv_file_path) as file:
            data = pd.read_csv(file)
        data.to_json(destination, orient='records')
    except IOError:
        print("Failed to convert csv file to json")
    except:
        print("Fatal error occurred while converting csv file to json")


def to_json(csv_file_path=""):
    try:
        with open(csv_file_path) as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return json.dumps(data)
    except IOError:
        print("Failed to convert csv file to json object")
        return []
    except:
        print("Fatal error occurred while converting csv file to json")
        return []
