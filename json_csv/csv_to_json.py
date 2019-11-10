import asyncio
import pandas as pd


async def to_json(csv_file_path="", destination=""):
    try:
        with open(csv_file_path) as file:
            data = pd.read_json(file)
        data.to_csv(destination, index=False)
    except IOError:
        print("Failed to convert csv file to json")


loop = asyncio.get_event_loop()
loop.run_until_complete(to_json(csv_file_path="../", destination="../"))
loop.close()
