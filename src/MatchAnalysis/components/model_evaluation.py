
import pickle
import mlflow
import pandas as pd
from pathlib import Path
from urllib.parse import urlparse
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from src.MatchAnalysis.utils.common import save_json
from src.MatchAnalysis.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def get_data(self):
        self.training_data = pd.read_csv(self.config.training_data)
        
    def train_valid_data_split(self):

        self.X = self.training_data[self.config.feature_columns]
        self.y = self.training_data[self.config.target_column]
        
        self.train_X, self.valid_X, self.train_y, self.valid_y = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.config.random_state
        )

    @staticmethod
    def load_model(path: Path) -> LogisticRegression:
        return pickle.load(open(path, 'rb'))
    
    def evaluate(self):
        self.model = self.load_model(self.config.model_path)
        self.train_valid_data_split()
        self.score = self.model.score(self.valid_X, self.valid_y)

        self.save_score()


    def save_score(self):
        scores = {
            "accuracy": self.score
        }

        save_json(path='scores.json', data=scores)


    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_registry_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)

            mlflow.log_metrics({
                "accuracy": self.score
            })

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(self.model, "model", registered_model_name="LogisticRegression")
            else:
                mlflow.sklearn.log_model(self.model, "model")
