from src.MatchAnalysis import logger
from src.MatchAnalysis.components.data_ingestion import DatatIngestion
from src.MatchAnalysis.config.configuration import ConfigurationManager

STAGE_NAME = 'Data Ingestion'

class DatatIngestionTrainingPieline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DatatIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = DatatIngestionTrainingPieline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
    except Exception as e:
        logger.error(e)
        raise e