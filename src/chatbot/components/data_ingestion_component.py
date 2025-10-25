import kagglehub
import os
import zipfile
from pathlib import Path
from src.chatbot import logger
from src.chatbot.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> Path:
        kagglehub.authenticate()  # Ensure you have your Kaggle API token set up
        logger.info(f"Downloading file from {self.config.source_url} to {self.config.root_dir}")
        dataset_path = kagglehub.dataset_download_files(self.config.source_url, path=self.config.root_dir, unzip=False)
        return Path(dataset_path)

    def extract_zip(self, zip_path: Path) -> None:
        logger.info(f"Extracting zip file {zip_path} to directory {self.config.unzip_dir}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Extraction completed successfully to directory {self.config.unzip_dir}")

    def initiate_data_ingestion(self) -> Path:
        zip_path = self.download_data()
        self.extract_zip(zip_path)
        return self.config.unzip_dir