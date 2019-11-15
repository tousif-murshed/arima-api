import pymongo
from os import environ
import pandas as pd


def fetch_training_set(training_data_path):
    try:
        print("connection string", environ.get("MONGO_CONNECTION"))
        client = pymongo.MongoClient(
            "mongodb+srv://default:gIt0f8tDqjnvnJfr@cluster0-um8zf.azure.mongodb.net/history?retryWrites=true&w=majority")
        db = client.history
        training_set = db.training_set
        data = list(data for data in training_set.find())
        df = pd.DataFrame(data, columns=['date', 'unitSold'])
        df.to_csv(training_data_path, index=False)
    except Exception as e:
        print("Unable to fetch training data {}".format(e))
