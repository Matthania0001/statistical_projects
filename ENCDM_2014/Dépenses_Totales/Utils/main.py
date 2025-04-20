from Cleaning import Donnee
from Histogramme import Histogramme
from regression import RegressionPlotly
import pieplot as pp
from boxplot import BoxPlot
from dashbord import create_px_dashboard
import pandas as pd
import plotly.express as px


# a = Donnee("../cleanedData/Data_wtout_na.xlsx", ".xlsx")
# a._load_data()
# b = a.df
# b["Profession_agreg_CM"] = b["Profession_agreg_CM"].fillna("Inactif")
# liste = b["Profession_agreg_CM"].unique()
# for i in range(len(liste)):
#     q = liste[i]
#     l = []
#     for j in range(len(b)):
#         if b["Profession_agreg_CM"][j] == q:
#             l += [b["DAM"][j]]
#     fig = px.histogram(
#         x = l,
#         title = f"Distribution de DAM pour la catégorie: {q}",
#         labels={'x': 'Valeurs', 'y': 'Fréquence'},
#     )
#     fig.update_layout(
#     bargap=0.05,  # Espace entre barres
#     hovermode="x unified"  # Infos groupées au survol
#     )
#     fig.show()
# a.remove_empty(["DAM", "Profession_agreg_CM"])
# t = pp.PiePlot(a.df, "Profession_agreg_CM")
# t.show(title="Répartition par Profession pour les Chefs de Ménages actifs")
# a.remove_duplicates()
# a.remove_outliers("DAM")
# a.remove_outliers("Age_CM")
# a.remove_outliers("DAM_G1")
# a.remove_outliers("DAM_G2")
# a.remove_outliers("DAM_G3")
# a.remove_outliers("DAM_G4")
# a.remove_outliers("DAM_G5")
# a.remove_outliers("DAM_G6")
# a.remove_outliers("DAM_G7")
# a.remove_outliers("DAM_G8")
# a.remove_outliers("DAM_G9")
# a.remove_outliers("Age_CM")
# print(a.df.columns)

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
# liste = ["square_DAM", "log_DAM", "racine_DAM", "inverse_DAM", "z_score_DAM", "func_gauss_DAM", "box_cox_DAM"]
# d = Histogramme("donnees_apres_transfo.xlsx", "Sheet1")
# d.charger_donnees()
# for i in range(len(liste)):
#     d.tracer_histogramme(
#         colonne=liste[i],
#         titre_graphe= f"Répartition des valeurs de {liste[i]}",
#         titre_x= f"Valeurs de {liste[i]}",
#         titre_y="Nombre d'occurences"
#     )
#     d.afficher()
# Données
valeurs = [52678.11731652004, 58213.65644129978, 65465.99347454085, 98465.23601490949,  81420.23187370396, 80625.9597820045, 206243.31743811502,  61785.670720720715, 69098.14545454545]
categories = ["Manœuvres non agricoles, manutentionnaires et  travailleurs des petits métiers",
              "Exploitants et ouvriers agricoles (y compris pêche, chasse et forêt)", 
              "Artisans et ouvriers qualifies et conducteurs d'installations et de machines et ouvriers  de l'assemblage", 
              "Cadres moyens et employés de bureau", 
              "Commerçants, intermédiaires commerciaux  et financiers", 
              "Inactifs",
              "Directeurs et cadres de direction, membres des corps législatifs,cadres supérieurs et membres des professions ", 
              "Chômeur n'ayant jamais travaillés", 
              "Non déclaré"]

# Création du bar plot
# fig = px.bar(
#     x=categories,
#     y=valeurs,
#     title="Répartition des dépenses annuelles par ménage par CSP",
#     labels={'x': 'Catégorie socioprofessionnelle', 'y': 'DAM par ménage'},
#     color=categories,  
#     text=valeurs,

# )
# fig.update_xaxes(showticklabels=False) 
# # Personnalisation supplémentaire
# fig.update_traces(texttemplate='%{text}', textposition='outside')
# fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# # Affichage
# fig.show()
l = [107779428.02,185119427.48,206741607.39,154098094.36,115698149.49,322584465.08,99203035.68,4572139.63,3040318.4]
for i in l:
    print(i/1198836665.5300002)
