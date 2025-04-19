from Cleaning import Donnee
from statistical_projects.ENCDM_2014.Dépenses_Totales.Viz.Histogramme import Histogramme
from regression import RegressionPlotly
import pieplot as pp
from statistical_projects.ENCDM_2014.Dépenses_Totales.Viz.boxplot import BoxPlot
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
a.remove_outliers("Age_CM")
print(a.df.columns)

# target = "DAM"
# features = ["N_ménage"]
# regression = RegressionPlotly(a.df, target, features)
#regression.plot()
# print(list(a.df["Région_12"])[0])
# a = pp.PiePlot(a.df, "Age_quin_CM")
# g1 = a.plot( title = 'Répartition par Age_quin_CM')
# b = pp.PiePlot(a.df, "Etat_matrimonial_CM")
# g2 = b.plot( title = 'Répartition par Etat_matrimonial_CM')
# c = pp.PiePlot(a.df, "Niveau_scolaire_agreg_CM")
# g3 = c.plot( title = 'Répartition Niveau_scolaire_agreg_CM')
# d = pp.PiePlot(a.df, "Région_12")
# g4 = d.plot( title = 'Répartition par Région')
# liste = [g1,g2,g3,g4]
# w = create_px_dashboard(px_figures=liste, cols=1, title="Etude de la Dépense Totale des Ménages au Maroc en 2014", )
# regression.show()
# w.run(debug = False, port = 8050)

# box_plot = BoxPlot(data_path="../cleanedData/Data_wtout_na.xlsx")
# box_plot.create_box_plot(title="Distribution de DAM", yaxis_title="Valeurs de DAM")
# box_plot.show()
liste = ["square_DAM", "log_DAM", "racine_DAM", "inverse_DAM", "z_score_DAM", "func_gauss_DAM", "box_cox_DAM"]
d = Histogramme("donnees_apres_transfo.xlsx", "Sheet1")
d.charger_donnees()
for i in range(len(liste)):
    d.tracer_histogramme(
        colonne=liste[i],
        titre_graphe= f"Répartition des valeurs de {liste[i]}",
        titre_x= f"Valeurs de {liste[i]}",
        titre_y="Nombre d'occurences"
    )
    d.afficher()