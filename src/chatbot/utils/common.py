import os
from pathlib import Path
from typing import Any, Union
import json
import yaml
import box.exceptions as BoxValueError
from ensure import ensure_annotations
from src.chatbot import logger
from typing import Dict, List
from box import ConfigBox

@ensure_annotations
def read_json(file_path: Union[str, Path]) -> Any:
    try:
        """Read a JSON file and return its contents.

        Args:
            file_path (Union[str, Path]): Path to the JSON file."""
        logger.info(f"Reading JSON file from {file_path}")
        with open(file_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except Exception as e:
        logger.error(f"Error reading JSON file from {file_path}: {e}")
        raise e
    
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        e: EmptyFileError if yaml file is empty
        e: YAMLError if yaml file is malformed

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise e
    
@ensure_annotations
def write_json(file_path: Union[str, Path], data: Any) -> None:
    try:
        """Write data to a JSON file.

        Args:
            file_path (Union[str, Path]): Path to the JSON file.
            data (Any): Data to write to the JSON file."""
        logger.info(f"Writing data to JSON file at {file_path}")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    except Exception as e:
        logger.error(f"Error reading YAML file from {file_path}: {e}")
        raise e

@ensure_annotations
def write_yaml(file_path: Union[str, Path], data: Any) -> None:
    try:
        """Write data to a YAML file.

        Args:
            file_path (Union[str, Path]): Path to the YAML file.
            data (Any): Data to write to the YAML file."""
        logger.info(f"Writing data to YAML file at {file_path}")
        with open(file_path, "w", encoding="utf-8") as yaml_file:
            yaml.safe_dump(data, yaml_file)
    except Exception as e:
        logger.error(f"Error reading YAML file from {file_path}: {e}")
        raise e

def create_directory(path_to_directories: list, verbose: bool = True) -> None:
    """Creates list of directories

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool, optional): Whether to log the directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def load_config(config_path: Union[str, Path]) -> ConfigBox:
    try:
        """Load configuration from a YAML file into a Box object.

        Args:
            config_path (Union[str, Path]): Path to the configuration YAML file."""
        logger.info(f"Loading configuration from {config_path}")
        config_data = read_yaml(config_path)
        return ConfigBox(config_data)
    except Exception as e:
        logger.error(f"Error loading configuration from {config_path}: {e}")
        raise e