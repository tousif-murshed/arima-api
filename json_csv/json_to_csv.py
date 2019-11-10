import json
import csv


def to_csv(json_object={}, json_file="", destination=""):
    if json_object:
        return json_object_to_csv(json_object, destination)
    elif json_file:
        return json_file


def json_object_to_csv(json_object, destination):
    try:
        sanitized_json = json.dumps(json_object)
        loaded_json = json.loads(sanitized_json)
        headers = loaded_json.keys()
        with open(destination, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for data in loaded_json:
                writer.writerow(data)
    except IOError:
        print("I/O error")


to_csv({"week": "1", "date": "01-01-1985", "unitSold": 100}, "", "./test.csv")
