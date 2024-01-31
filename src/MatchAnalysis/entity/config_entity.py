from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_n_jobs: int


@dataclass(frozen=True)
class PrepareDataConfig:
    root_dir: Path
    raw_data_path: Path
    prepared_data_path: Path
    feature_columns: list
    target_column: str


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    feature_columns: list
    target_column: str
    n_jobs: int
    random_state: int


@dataclass(frozen=True)
class EvaluationConfig:
    model_path: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    random_state: int
    feature_columns: list
    target_column: str

    