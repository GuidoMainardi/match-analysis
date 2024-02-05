import os
import pickle
import pandas as pd

class PredictionPipeline:

    def __init__(self):
        pass

    @staticmethod
    def predict(sample):

        # load model
        model = pickle.load(open(os.path.join('artifacts', 'training', 'model.pkl'), 'rb'))

        #load scaler
        scaler = pickle.load(open(os.path.join('artifacts', 'prepare_data', 'scaler.pkl'), 'rb'))

        # load data
        data = pd.DataFrame.from_dict(sample)

        # scale data
        data = scaler.transform(data)

        # predict
        result = model.predict(data)

        if result[0] == 0:
            prediction = 'Blue team wins'
        else:
            prediction = 'Red team wins'

        return [{'prediction': prediction}]