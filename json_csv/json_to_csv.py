import json
import csv
import pandas as pd
import asyncio


async def to_csv(json_object=None, json_file_path="", destination=""):
    if json_object:
        await json_object_to_csv(json_object, destination)
    elif json_file_path:
        await json_file_to_csv(json_file_path, destination)


async def json_object_to_csv(json_object, destination):
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


async def json_file_to_csv(json_file_path, destination):
    try:
        with open(json_file_path) as file:
            data = pd.read_json(file)
        data.to_csv(destination, index=False)
    except IOError:
        print("Failed to convert json file to csv")


loop = asyncio.get_event_loop()
loop.run_until_complete(
    to_csv(
        json_object=[{"week": "1", "date": "01-01-1985", "unitSold": 100},
                     {"week": "1", "date": "01-01-1986", "unitSold": 200}],
        destination="../test.csv")
)
loop.run_until_complete(
    to_csv(
        json_file_path="../data.json",
        destination="../data.csv")
)
loop.close()
