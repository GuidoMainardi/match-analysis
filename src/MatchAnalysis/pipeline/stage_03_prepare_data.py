from src.MatchAnalysis import logger
from src.MatchAnalysis.components.prepare_data import PrepareData
from src.MatchAnalysis.config.configuration import ConfigurationManager

STAGE_NAME = 'Prepare Data'

class PrepareDataPieline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_data_config = config.get_prepare_data_config()
        prepare_data = PrepareData(prepare_data_config)
        prepare_data.get_data()
        prepare_data.get_scaler()
        prepare_data.update_data()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = PrepareDataPieline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<')
    except Exception as e:
        logger.error(e)
        raise e