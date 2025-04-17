from Cleaning import Donnee
from regression import RegressionPlotly
import pieplot as pp
from dashbord import create_px_dashboard
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
# regression.fit()
regression.plot()
# print(list(a.df["Région_12"])[0])
a = pp.PiePlot(a.df, "Age_quin_CM")
g1 = a.plot( title = 'Répartition de la taille des ménages')
b = pp.PiePlot(a.df, "Age_quin_CM")
g2 = b.plot( title = 'Répartition de la taille des ménages')
c = pp.PiePlot(a.df, "Age_quin_CM")
g3 = b.plot( title = 'Répartition de la taille des ménages')
liste = [g1,g2,g3]
w = create_px_dashboard(px_figures=[regression.plot()[1]]+liste, cols=1)
#regression.show()
w.run(debug = False, port = 8050)