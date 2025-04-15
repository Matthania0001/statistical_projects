#Importation des données
library(haven)  
library(dplyr)
library(tidyr)
library(writexl)
library(ggplot2)
df <- read_sav("../Data/data_ENCDM_2014.sav")  
# Affichage des 6 premières lignes du jeu de données
#print(df)
#Exploration des données 
#glimpse(df)      # Structure des données  
#summary(df)      # Résumé statistique  
#colSums(is.na(df))  # Compte des NA par colonne  

#Gestion des valeurs manquantes
df_clean <- df[complete.cases(df[, c("DAM")]), ]
 # Suppression des lignes contenant des valeurs manquantes
df_clean <- df_clean %>% mutate(DAM = ifelse(DAM < 0, 0, DAM)) # Remplace les valeurs négatives par 0
print(df_clean)
#Detection des outliers

# Boxplot visuel  
boxplot <- ggplot(df, aes(y = DAM)) +
  geom_boxplot() +
  labs(title = "Boxplot des Dépenses Annuelles")

# Sauvegarder en PNG (haute qualité)
ggsave("../DataViz/boxplot_DAM.png", plot = boxplot, width = 8, height = 6, dpi = 300)

# Sauvegarder en PDF (vectoriel, idéal pour les rapports)
ggsave("../DataViz/boxplot_DAM.pdf", plot = boxplot, width = 8, height = 6)
#Variable cible : DAM
Q1 <- quantile(df$DAM, 0.25)  
Q3 <- quantile(df$DAM, 0.75)  
IQR <- Q3 - Q1  
print(Q1 - IQR) 
df_wt_outliers <- df_clean %>% filter(as.numeric(DAM) >= Q1 - 1.5*IQR & as.numeric(DAM) <= Q3 + 1.5*IQR)  
#print(df_wt_outliers) 
#Creation de variables dérivées
df_wt_outliers <- df_wt_outliers %>%
  mutate(
    DAM = as.numeric(DAM),
    Taille_agregée = as.numeric(Taille_agregée),
    Age_CM = as.numeric(Age_CM)
  )
df_add_variables <- df_wt_outliers %>%  
  mutate(  
    Dépenses_par_personne = DAM / Taille_agregée,  
    Catégorie_âge = cut(Age_CM, breaks = c(20, 40, 60, 80), labels = c("Jeune", "Adulte", "Âgé"))  
  )  
#print(df_add_variables)
#exportation des données nettoyées avec les nouvelles variables 
write_sav(
  df_add_variables,
  "../Data/donnees_nettoyée_DAM.sav",
)
write_xlsx(
  list("Feuille1" = df_add_variables),
  "../Data/donnees_nettoyées_DAM.xlsx"
)
