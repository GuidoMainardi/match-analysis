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