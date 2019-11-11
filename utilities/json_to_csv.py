import csv
import json
import pandas as pd


def to_csv(json_object=None, json_file_path="", destination=""):
    if json_object:
        json_object_to_csv(json_object, destination)
    elif json_file_path:
        json_file_to_csv(json_file_path, destination)


def json_object_to_csv(json_object, destination):
    try:
        sanitized_json = json.dumps(json_object)
        loaded_json = json.loads(sanitized_json)
        headers = loaded_json[0].keys() if loaded_json[0] else ""
        with open(destination, "w") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for data in loaded_json:
                writer.writerow(data)
    except IOError:
        print("Failed to convert json object to csv")
    except:
        print("Fatal error occurred while converting json object to csv")


def json_file_to_csv(json_file_path, destination):
    try:
        with open(json_file_path) as file:
            data = pd.read_json(file)
        data.to_csv(destination, index=False)
    except IOError:
        print("Failed to convert json file to csv")
    except:
        print("Fatal error occurred while converting json file to csv")
