import pickle
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from src.MatchAnalysis.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        file = open(self.config.updated_base_model_path, 'rb')
        self.model = pickle.load(
            file
        )

    def get_data(self):
        self.training_data = pd.read_csv(self.config.training_data)
        
    def train_valid_data_split(self):

        self.X = self.training_data[self.config.feature_columns]
        self.y = self.training_data[self.config.target_column]
        
        self.train_X, self.valid_X, self.train_y, self.valid_y = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.config.random_state
        )

    def train(self):

        self.model.fit(self.train_X, self.train_y)

        self.save_model(
            self.config.trained_model_path,
            self.model
        )

        self.save_model(
            self.config.trained_model_container,
            self.model
        )

    @staticmethod
    def save_model(path: Path, model):
        with open(path, 'wb') as f:
            pickle.dump(model, f)