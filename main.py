from src.MatchAnalysis import logger
from src.MatchAnalysis.pipeline.stage_01_data_ingestion import DatatIngestionTrainingPieline


STAGE_NAME = 'Data Ingestion'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = DatatIngestionTrainingPieline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
except Exception as e:
    logger.error(e)
    raise e