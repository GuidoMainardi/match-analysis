import os
import gdown
import zipfile


from src.MatchAnalysis import logger
from src.MatchAnalysis.entity.config_entity import DataIngestionConfig

class DatatIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """ 
        Fetch data from the url
        """

        try:
            dataset_url = self.config.source_URL
            csv_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f'Downloading data from {dataset_url} to {csv_download_dir}')

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export-download&id='
            gdown.download(prefix + file_id, csv_download_dir)

            logger.info(f'downloaded data from {dataset_url} to {csv_download_dir}')

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip file into the data directory
        function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)