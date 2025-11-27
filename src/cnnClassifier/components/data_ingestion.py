import os
import zipfile
import gdown
import logging

from src.cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import (DataIngestionConfig)

logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self) -> str:
        """
        Download a ZIP file from Google Drive
        """
        try:
            zip_url = self.config.source_URL        # direct ZIP file link
            zip_path = self.config.local_data_file  # artifacts/data_ingestion/kidney_dataset.zip

            os.makedirs(self.config.root_dir, exist_ok=True)

            logger.info(f"Downloading ZIP from {zip_url} into {zip_path}")

            gdown.download(zip_url, str(zip_path), quiet=False)

            logger.info(f"Downloaded ZIP file at: {zip_path}")

            return zip_path
        
        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        Extract the downloaded ZIP file into unzip_dir
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            logger.info(f"Extracting ZIP file {self.config.local_data_file} into {unzip_path}")

            # ⚠ Only works if the file is a real ZIP
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"Extraction completed at {unzip_path}")

        except zipfile.BadZipFile:
            logger.error("The downloaded file is not a valid ZIP file. Please check the source_URL")
            raise
        except Exception as e:
            raise e