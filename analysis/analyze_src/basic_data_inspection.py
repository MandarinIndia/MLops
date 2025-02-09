from abc import ABC , abstractmethod
import pandas as pd

# Abstract Base Class for Data Inspection Strategies.
#This class defines the common interface for data inspection strategy.
#Subclasses must implement the inspect methods.
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self , df : pd.DataFrame):
        """
        Perform a specific type of data inspection

        Parameters:
        df(pd.DataFrame) : The dataframe for inspection to be performed

        Returns:
        None : This method prints the inspection directly
        """
        pass


#Concrete Strategies for data inspections
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self , df : pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts to the console.
        """
        print("\n Data Types and Non-null Counts")
        print(df.info())


#Concrete strategy for Summary Statistics Inspection
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self , df : pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints summary statistics to the console.
        """
        print("\nSummary Statistics (Numerical Features)")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features)")
        print(df.describe(include=["O"]))


#Context Class that uses a DataInspectionStrategy

class DataInspector:
    def __init__(self , strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self.strategy = strategy

    def set_strategy(self , strategy:DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """ 
        self.strategy = strategy

    def execute_inspection(self , df : pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """
        self.strategy.inspect(df)


if __name__ == "main":
    # Load the data
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Initialize the Data Inspector with a specific strategy
    # inspector = DataInspector(DataTypesInspectionStrategy())
    # inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    # inspector.execute_inspection(df)
    pass
