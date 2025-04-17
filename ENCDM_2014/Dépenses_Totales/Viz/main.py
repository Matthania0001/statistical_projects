from Cleaning import Donnee
from regression import RegressionPlotly
a = Donnee("../cleanedData/Data_wtout_na.xlsx", ".xlsx")
a._load_data()
a.remove_empty(["DAM", "Age_CM"])
a.remove_duplicates()
a.remove_outliers("DAM")
a.remove_outliers("Age_CM")
a.remove_outliers("DAM_G1")
a.remove_outliers("DAM_G2")
a.remove_outliers("DAM_G3")
a.remove_outliers("DAM_G4")
a.remove_outliers("DAM_G5")
a.remove_outliers("DAM_G6")
a.remove_outliers("DAM_G7")
a.remove_outliers("DAM_G8")
a.remove_outliers("DAM_G9")

target = "DAM"
features = ["DAM_G1","DAM_G2", "DAM_G3", "DAM_G4", "DAM_G5", "DAM_G6", "DAM_G7", "DAM_G8", "DAM_G9"]
regression = RegressionPlotly(a.df, target, features)
regression.fit()
regression.plot()