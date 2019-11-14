import pymongo
from os import environ
import pandas as pd


def fetch_training_set(training_data_path):
    try:
        client = pymongo.MongoClient(environ.get("MONGO_CONNECTION"))
        db = client.history
        training_set = db.training_set
        data = list(data for data in training_set.find())
        df = pd.DataFrame(data, columns=['date', 'unitSold'])
        df.to_csv(training_data_path, index=False)
    except Exception as e:
        print("Unable to fetch training data {}".format(e))
