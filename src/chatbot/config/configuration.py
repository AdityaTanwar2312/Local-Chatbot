from pathlib import Path
import os
from src.chatbot.constants import *
from src.chatbot.utils.common import read_yaml, create_directory
from src.chatbot.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directory([self.config[self.config.artifact_root]])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            unzip_dir=Path(config.unzip_dir)
        )
        return data_ingestion_config