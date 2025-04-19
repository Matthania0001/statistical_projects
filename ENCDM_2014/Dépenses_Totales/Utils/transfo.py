from pandas import DataFrame
class Transformation:
    def __init__(self, df:DataFrame, func: list[callable], columns:list[str]):
        self.df = df
        self.functions = func
        self.columns = columns
        self.df_transformed = None
    def transformation(self):
        for j in range(len(self.functions)):
            for i in range(len(self.columns)):
                self.df[f"{self.functions[j].__name__}_{self.columns[i]}"] = self.functions[j](self.df[f"{self.columns[i]}"])
        return "Colonnes ajoutées"
    def save_excel(self, file_name = "donnees_apres_transfo.xlsx"):
        self.df.to_excel(file_name, index = False)
            
        