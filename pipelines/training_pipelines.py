from steps.data_ingestion_step import data_ingestion_step
from zenml import Model , pipeline , step
@pipeline(
    model = Model(name = "Price Predictor"),
)

def ml_pipeline():
    """Define an end to end machine learning pipeline"""

    #Data Ingestion step
    raw_data = data_ingestion_step(
        file_path = 'Data/archive.zip'
    )

    #Handling missing values Step
    