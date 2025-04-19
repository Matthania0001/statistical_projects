from typing import Optional, List
import pandas as pd
import numpy as np

class Donnee:
    def __init__(self, file_name: str, file_type: str) -> None:
        """
        Initialise l'objet Donnee avec le nom et le type de fichier.
        """
        self.file_name: str = file_name
        self.file_type: str = file_type
        self.df: pd.DataFrame = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        """
        Charge les données en fonction du type de fichier.
        """
        if self.file_type == ".sas":
            return pd.read_sas(self.file_name)
        elif self.file_type == ".sav":
            return pd.read_spss(self.file_name)
        elif self.file_type == ".csv":
            return pd.read_csv(self.file_name)
        elif self.file_type == ".xlsx":
            return pd.read_excel(self.file_name)
        elif self.file_type == ".json":
            return pd.read_json(self.file_name)
        elif self.file_type == ".txt":
            return pd.read_csv(self.file_name, sep="\t")
        elif self.file_type == ".html":
            return pd.read_html(self.file_name)[0]
        elif self.file_type == ".xml":
            return pd.read_xml(self.file_name)
        elif self.file_type == ".parquet":
            return pd.read_parquet(self.file_name)
        else:
            raise ValueError("Unsupported file type")

    def remove_empty(self, column_names: Optional[List[str]] = None) -> None:
        """
        Supprime les lignes avec des valeurs manquantes.
        """
        if column_names is None or len(column_names) == 0:
            self.df = self.df.dropna()
        else:
            self.df = self.df.dropna(subset=column_names)

    def remove_duplicates(self) -> None:
        """
        Supprime les doublons.
        """
        self.df = self.df.drop_duplicates()

    def remove_columns_by_variable(self, column_names: List[str]) -> None:
        """
        Supprime des colonnes spécifiques.
        """
        if column_names:
            self.df = self.df.drop(columns=column_names)

    def remove_columns_by_sequence(self, start: Optional[int] = None, end: Optional[int] = None) -> None:
        """
        Supprime des colonnes par séquence.
        """
        if start is None and end is None:
            return
        elif start is not None and end is None:
            if 0 <= start < len(self.df.columns):
                self.df = self.df.drop(columns=self.df.columns[start:])
            else:
                raise IndexError("Start index out of range")
        elif start is None and end is not None:
            if 0 <= end < len(self.df.columns):
                self.df = self.df.drop(columns=self.df.columns[:end + 1])
            else:
                raise IndexError("End index out of range")
        else:
            if 0 <= start <= end < len(self.df.columns):
                self.df = self.df.drop(columns=self.df.columns[start:end + 1])
            else:
                raise IndexError("Start or end index out of range")

    def remove_outliers(self, var: str) -> None:
        """
        Supprime les valeurs aberrantes d'une colonne.
        """
        if var not in self.df.columns:
            raise ValueError(f"La colonne '{var}' n'existe pas dans le DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.df[var]):
            raise TypeError(f"La colonne '{var}' doit être de type numérique pour calculer les quantiles.")
        
        Q1: float = self.df[var].quantile(0.25)
        Q3: float = self.df[var].quantile(0.75)
        IQR: float = Q3 - Q1
        lower_bound: float = Q1 - 1.5 * IQR
        upper_bound: float = Q3 + 1.5 * IQR
        self.df = self.df[(self.df[var] >= lower_bound) & (self.df[var] <= upper_bound)]

    def display(self, head: int = 5) -> pd.DataFrame:
        """
        Affiche les premières lignes du DataFrame nettoyé.

        Args:
            head (int): Le nombre de lignes à afficher. Par défaut, 5.

        Returns:
            pd.DataFrame: Les premières lignes du DataFrame.
        """
        if self.df.empty:
            print("Le DataFrame est vide.")
            return pd.DataFrame()  # Retourne un DataFrame vide pour éviter les erreurs
        return self.df.head(head)

    def export(self, output_path: str) -> None:
        """
        Exporte les données nettoyées vers un fichier Excel.
        """
        self.df.to_excel(output_path, index=False)