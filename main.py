from src.MatchAnalysis import logger
from src.MatchAnalysis.pipeline.stage_01_data_ingestion import DatatIngestionTrainingPieline
from src.MatchAnalysis.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = 'Data Ingestion'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = DatatIngestionTrainingPieline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
except Exception as e:
    logger.error(e)
    raise e





STAGE_NAME = 'Prepare base model'
try:
    logger.info(f'*'*20)
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
except Exception as e:
    logger.error(e)
    raise e