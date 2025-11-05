from src.chatbot.components.data_ingestion_component import DataIngestion
from src.chatbot.config.configuration import ConfigurationManager
from src.chatbot import logger

STAGE_NAME = "Stage Name ----> Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.initiate_data_ingestion()

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>> Data Ingestion >>>>>>>>>>>>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(">>>>>>>>>>>>> Data Ingestion Complete >>>>>>>>>>>>>")

    except Exception as e:
        logger.exception(e)
        raise e