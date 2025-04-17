import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

class RegressionPlotly:
    def __init__(self, df, target_column, feature_columns):
        self.df = df
        self.target_column = target_column
        self.feature_columns = feature_columns
        self.model = LinearRegression()

    def fit(self):
        X = self.df[self.feature_columns]
        y = self.df[self.target_column]
        self.model.fit(X, y)
        self.df['prediction'] = self.model.predict(X)

    def plot(self):
        for feature in self.feature_columns:
            fig = px.scatter(self.df, x=feature, y=self.target_column,
                             trendline='ols', title=f'{feature} vs {self.target_column}')
            fig.show()

# Exemple avec le jeu de données Iris
