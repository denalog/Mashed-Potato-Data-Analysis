from abc import ABC, abstractmethod
import pandas as pd

class FeatureEngineeringRepository(ABC):
    '''''
    @abstractmethod
    def handleMissingValues(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
    '''''

    @abstractmethod
    def encodeCategoricalFeatures(self, data: pd.DataFrame) -> (pd.DataFrame, dict):
        pass

    @abstractmethod
    def createNewFeatures(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def savePreprocessedData(self, data: pd.DataFrame, file_path: str):
        pass

    @abstractmethod
    def splitTrainTestData(self, data: pd.DataFrame):
        pass


    @abstractmethod
    def scaleFeatures(self, X_train, X_test):
        pass


    @abstractmethod
    def trainModel(self, X_train, y_train):
        pass

    @abstractmethod
    def evaluateModel(self, model, X_test, y_test):
        pass

    @abstractmethod
    def compareResult(self, y_test, y_prediction):
        pass

    @abstractmethod
    def crossValidateModel(self, model, X, y, cv: int = 5):
        pass

    @abstractmethod
    def plotFeatureImportance(self, model, feature_names):
        pass

