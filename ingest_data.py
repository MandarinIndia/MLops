#Importing Libraries
import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# Define abstract class for data ingrestion
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self , file_path : str) -> pd.DataFrame:
        pass


# Implement a concrete class for zip Ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self , file_path : str) -> pd.DataFrame:
        if not file_path.endswith(".zip"):
            raise ValueError("Provided file is not zip file")
        
        with zipfile.ZipFile(file_path , "r") as zip_ref:
            zip_ref.extractall("ExtractedData")
        
        extracted_files = os.listdir("ExtractedData")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No csv file found")
        if len(csv_files) > 1:
            raise ValueError("Multiple csv files found. Please specify")

        csv_file_path = os.path.join("ExtractedData" , csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df


#Implement factory to create DataIngestors
class DataIngetorFactory:
    @staticmethod
    def get_data_ingestor(file_extension : str):
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError("No ingestor available for file extension: {file_extension}")


# Main function to test the code
if __name__ == "__main__":
    file_path = "Data/archive.zip"
    file_extension = os.path.splitext(file_path)[1]
    data_ingestor = DataIngetorFactory.get_data_ingestor(file_extension)
    df = data_ingestor.ingest(file_path)
    print(df.head())
    pass
