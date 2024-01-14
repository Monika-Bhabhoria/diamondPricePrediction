import pandas as pd
import numpy as np
import sys
import os
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class dataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config=dataIngestionConfig()

    def init_data_ingestion(self):
        logging.info("Starting data ingestion")

        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","train.csv")))
            logging.info("Data read successfully")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw data saved in artifact table")

            logging.info("Performing train test split")
            train_data,test_data=train_test_split(data,test_size=0.2)
            logging.info("train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data Ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info("Exception caught during data ingestion phase")
            raise customException(e,sys)

