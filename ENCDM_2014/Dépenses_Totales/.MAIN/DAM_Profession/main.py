import pandas as pd
import numpy as np
from Cleaning import Donnee
a = Donnee("../../cleanedData/Data_wtout_na.xlsx", ".xlsx")
a._load_data()
a.df["Profession_agreg_CM"] = a.df["Profession_agreg_CM"].fillna("Inactif")
b = a.df
#b.to_excel("AAA.xlsx", index=False)
liste = []
valeur = []
for i in range(len(b)):
    if b["Profession_agreg_CM"][i] == "Inactif" and b["Type_activité_dominante_CM"][i] not in liste:
        liste += [b["Type_activité_dominante_CM"][i]]
print(liste)
for i in liste:
    valeur +=[list(b["Type_activité_dominante_CM"]).count(i)]
import plotly.express as px

# Données
labels = liste
values = valeur

# Créer le pie chart
fig = px.pie(
    names=labels, 
    values=values,
    title="Répartition des chef de ménages inactifs"
)

# Afficher
fig.show()
# for i in range(0, len(b)):
#     if list(b["Profession_agreg_CM"])[i] not in liste:
#         liste.append(list(b["Profession_agreg_CM"])[i])
# liste_0 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[0]]
# liste_1 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[1]]
# liste_2 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[2]]
# liste_3 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[3]]
# liste_4 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[4]]
# liste_5 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[5]]
# liste_6 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[6]]
# liste_7 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[7]]
# liste_8 = [list(b["DAM"])[i] for i in range(len(b)) if list(b["Profession_agreg_CM"])[i]==liste[8]]
# c = [liste_0, liste_1, liste_2, liste_3, liste_4, liste_5, liste_6, liste_7, liste_8]
# print("DAM par profession")
# def info_profession(w):
#     for i in range(len(w)):
#         print(f"Profession: {liste[i]}")
#         # print(f"Moyenne: {np.mean(w[i])}")
#         # print(f"Variance: {np.var(w[i])}")
#         # print(f"Mediane: {np.median(w[i])}")
#         # print(f"Max: {np.max(w[i])}")
#         # print(f"Min: {np.min(w[i])}")
#         #print(f"Somme: {np.sum(w[i])}")
#         print(f"Porcentage : {len(w[i])/len(b)}")
#         #print(f"Dépenses par Ménage: {np.sum(w[i])/len(w[i])}")
#         print("----------------------------------------------------------------")
# info_profession(c)

# import plotly.express as px
# import pandas as pd
# fig = px.box(
#     b,
#     x="Profession_agreg_CM",
#     y="DAM",
#     title="Dépenses Annuelles (DAM) par Profession",
#     labels={"DAM": "Dépense Annuelle", "Profession": "Catégorie Professionnelle"},
#     color="Profession_agreg_CM",
#     hover_data=["Profession_agreg_CM"] 
# )
# fig.update_xaxes(showticklabels=False)
# fig.show()