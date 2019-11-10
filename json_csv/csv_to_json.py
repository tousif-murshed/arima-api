import asyncio
import pandas as pd
import csv
import json


async def to_json_file(csv_file_path="", destination=""):
    try:
        with open(csv_file_path) as file:
            data = pd.read_csv(file)
        data.to_json(destination, orient='records')
    except IOError:
        print("Failed to convert csv file to json")
    except Exception:
        print("Fatal error occurred while converting csv file to json")


async def to_json(csv_file_path=""):
    try:
        with open(csv_file_path) as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return json.dumps(data)
    except IOError:
        print("Failed to convert csv file to json object")
        return []
    except Exception:
        print("Fatal error occurred while converting csv file to json")
        return []


loop = asyncio.get_event_loop()
loop.run_until_complete(to_json_file(csv_file_path="../test.csv", destination="../data.json"))
loop.run_until_complete(to_json(csv_file_path="../test.csv"))
loop.close()
