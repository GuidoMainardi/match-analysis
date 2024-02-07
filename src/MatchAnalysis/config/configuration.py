from src.MatchAnalysis.constants import *
from src.MatchAnalysis.utils.common import read_yaml, create_directories

from src.MatchAnalysis.entity.config_entity import DataIngestionConfig
from src.MatchAnalysis.entity.config_entity import PrepareBaseModelConfig
from src.MatchAnalysis.entity.config_entity import PrepareDataConfig
from src.MatchAnalysis.entity.config_entity import TrainingConfig
from src.MatchAnalysis.entity.config_entity import EvaluationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir        = config.root_dir,
            source_URL      = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir       = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:


        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_n_jobs = self.params.N_JOBS
        )

        return prepare_base_model_config
    
    def get_prepare_data_config(self):

        prepare_data = self.config.prepare_data
        raw_data = self.config.data_ingestion.data_file

        create_directories([
            Path(prepare_data.root_dir)
        ])

        prepare_data_config = PrepareDataConfig(
            root_dir = Path(prepare_data.root_dir),
            raw_data_path = Path(raw_data),
            prepared_data_path = Path(prepare_data.prepared_data_path),
            base_scaler_path = Path(prepare_data.base_scaler_path),
            feature_columns = prepare_data.feature_columns,
            target_column = prepare_data.target_column
            
        )

        return prepare_data_config
    
    def get_training_config(self):

        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        training_data = self.config.prepare_data.prepared_data_path
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir = Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data = Path(training_data),
            trained_model_container = Path(training.trained_model_container),
            feature_columns = self.config.prepare_data.feature_columns,
            target_column = self.config.prepare_data.target_column,
            n_jobs = self.params.N_JOBS,
            random_state = self.params.VAL_SPLIT_RANDOM_STATE
        )
        
        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        evaluation_config = EvaluationConfig(
            model_path = self.config.training.trained_model_path,
            training_data = self.config.prepare_data.prepared_data_path,
            all_params = self.params,
            mlflow_uri = "https://dagshub.com/GuidoMainardi/match-analysis.mlflow",
            random_state = self.params.VAL_SPLIT_RANDOM_STATE,
            feature_columns = self.config.prepare_data.feature_columns,
            target_column = self.config.prepare_data.target_column
        )
        return evaluation_config