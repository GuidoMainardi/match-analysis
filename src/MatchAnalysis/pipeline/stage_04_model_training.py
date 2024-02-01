from src.MatchAnalysis import logger
from src.MatchAnalysis.components.model_training import Training
from src.MatchAnalysis.config.configuration import ConfigurationManager

STAGE_NAME = 'Model Training'

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_data()
        training.get_base_model()
        training.train_valid_data_split()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f'*'*20)
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
        logger.info('\nx====================x\n')
    except Exception as e:
        logger.error(e)
        raise e