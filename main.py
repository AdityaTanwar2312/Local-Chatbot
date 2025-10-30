from src.chatbot import logger
from src.chatbot.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Stage Name -----> Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>>> Data Ingestion >>>>>>>>>>>>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>> Data Ingestion Complete >>>>>>>>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e