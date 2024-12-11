import os
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    # def validate_all_columns(self) -> bool:
    #     try:
    #         validation_status = True  # Start with assuming validation passes

    #         # Load the dataset and schema
    #         data = pd.read_csv(self.config.unzip_data_dir)
    #         all_cols = list(data.columns)
    #         all_schema = self.config.all_schema

    #         # Iterate through schema to validate both column names and data types
    #         for col, expected_dtype in all_schema.items():
    #             if col not in all_cols:
    #                 validation_status = False
    #                 with open(self.config.STATUS_FILE, 'w') as f:
    #                     f.write(f"Column missing: {col}\n")
    #             else:
    #                 actual_dtype = str(data[col].dtype)
    #                 if actual_dtype != expected_dtype:
    #                     validation_status = False
    #                     with open(self.config.STATUS_FILE, 'w') as f:
    #                         f.write(f"Datatype mismatch for column '{col}': Expected {expected_dtype}, Found {actual_dtype}\n")

    #         # Write final validation status
    #         with open(self.config.STATUS_FILE, 'w') as f:
    #             f.write(f"Final Validation Status: {validation_status}\n")

    #         return validation_status

    #     except Exception as e:
    #         raise e

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
