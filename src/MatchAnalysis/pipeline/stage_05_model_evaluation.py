from src.MatchAnalysis import logger
from src.MatchAnalysis.components.model_evaluation import Evaluation
from src.MatchAnalysis.config.configuration import ConfigurationManager

STAGE_NAME = 'Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.get_data()
        evaluation.evaluate()
        #evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f'*'*20)
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
        logger.info('\nx====================x\n')
    except Exception as e:
        logger.error(e)
        raise e