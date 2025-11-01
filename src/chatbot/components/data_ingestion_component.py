from pathlib import Path
from src.chatbot import logger
from src.chatbot.entity.config_entity import DataIngestionConfig
from kaggle import api

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> Path:
        logger.info(f"Downloading file from {self.config.source_url} to {self.config.root_dir}")
        api.dataset_download_files(dataset=self.config.source_url, path=self.config.root_dir, unzip=True)
        
    def initiate_data_ingestion(self) -> Path:
        self.download_data()
        return self.config.unzip_dir