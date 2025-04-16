from Cleaning import Donnee
from Boxplot import plot_boxplot
'''a = Donnee(file_name = "../../Data/data_ENCDM_2014.sav",file_type = ".sav")
a.remove_empty(['DAM'])
a.remove_duplicates()
a.remove_columns_by_sequence(36, 791)
a.remove_outliers('DAM')
#a.export("../cleanedData/donnees_nett_DAM.xlsx")
#a.display()'''
# --------------------------------------------------
# Exemples d'utilisation :
# --------------------------------------------------

# 1. Pour une seule colonne
Df = Donnee(file_name="../../Data/data_ENCDM_2014.sav", file_type=".sav")
Df.remove_empty(['DAM'])
# Vérification et nettoyage des données
# Tracer un boxplot pour une colonne spécifique
plot_boxplot(Df.df, columns=['DAM'], orientation='horizontal', save_path= "../Viz/Boxplot_DAM.png")


