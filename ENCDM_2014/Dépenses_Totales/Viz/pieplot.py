import pandas as pd
import plotly.express as px
class PiePlot:
    def __init__(self, df: pd.DataFrame, column_name: str):
        self.df = df
        self.column_name = column_name
    def plot(self, title: str):
        # Compter les occurrences de chaque valeur dans la colonne
        value_counts = self.df[self.column_name].value_counts()
        # Créer le graphique en secteurs
        if title == None:
            fig = px.pie(value_counts, values=value_counts.values, names=value_counts.index, title=f'Répartition de {self.column_name}')
        else:
           fig = px.pie(value_counts, values=value_counts.values, names=value_counts.index, title=title) 
        return fig
    def show(self, title = None):
        a = self.plot(title=title)
        a.show()
    def save(self, filename: str, file_format: str = "html"):
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")