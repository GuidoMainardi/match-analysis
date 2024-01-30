import pandas as pd
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

from src.MatchAnalysis.config.configuration import PrepareDataConfig

class PrepareData:
    def __init__(self, config: PrepareDataConfig):
        self.config = config

    def _prepare_data(self):
        
        clean_data = self.data[
            [*self.config.feature_columns, 
              self.config.target_column]
        ]

        return pd.DataFrame(
            self.scaler.fit_transform(clean_data),
            columns = clean_data.columns
        )

        
    def get_data(self):
        self.data = pd.read_csv(self.config.raw_data_path)
    
    def get_scaler(self):
        self.scaler = MinMaxScaler()

    def update_data(self):

        self.normalized_data = self._prepare_data()

        self.save_data(
            path=self.config.prepared_data_path,
            data=self.normalized_data
        )

    @staticmethod
    def save_data(path: Path, data):
        data.to_csv(path, index=False)
