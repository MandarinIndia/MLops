from abc import ABC , abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Abstract Base Class for Missing Values Analysis

#This class defines a template for missing values analysis.
#Subclasses must implement the methods to identify and visualizes missing values
class MissingValuesAnalysisTemplate(ABC):
    def analyze(self , df : pd.DataFrame):
        """
        Performs a complete missing values analysis by identifying and visualizing missing values.

        Parameters:
        df (pd.DataFrame) : The dataframe to be analyzed

        Returns:
        None : This method performs tha analysis and visualizes missing values
        """

        self.identify_missing_values(df)
        self.visualize_missing_values(df)

        @abstractmethod
        def identify_missing_values(self , df : pd.DataFrame):
            """
            Identifies missing values in the dataframe.

            Parameters:
            df (pd.DataFrame): The dataframe to be analyzed.

            Returns:
            None: This method should print the count of missing values for each column.
            """
            pass

        @abstractmethod
        def visualize_missing_values(self, df: pd.DataFrame):
            """
            Visualizes missing values in the dataframe.

            Parameters:
            df (pd.DataFrame): The dataframe to be visualized.

            Returns:
            None: This method should create a visualization (e.g., heatmap) of missing values.
            """
            pass