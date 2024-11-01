from typing import List
import numpy as np


class LinearRegression:
    def __init__(self):
        self.X = None
        self.y = None
        self.theta = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.X = X
        self.y = y
        self.theta = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, X: np.ndarray) -> np.ndarray:
        return X @ self.theta

    



