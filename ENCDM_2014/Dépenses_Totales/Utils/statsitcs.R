library(R6)
library(readxl)
library(dplyr)
library(moments)
statistiques <- R6Class(
  classname = "Statistiques",
  public = list(
    file_name = NULL,
    sheet_name = NULL,
    data = NULL,
    # Constructeur
    initialize = function(file_name, sheet_name) {
      self$file_name <- file_name
      self$sheet_name <- sheet_name
      self$data <- readxl::read_excel(self$file_name, sheet = self$sheet_name)
    },
    # Méthode pour obtenir les données
    get_data = function() {
      self$data
    },
    # Méthode pour calculer les statistiques
    get_statistics = function(column_name) {
      # Vérification des arguments
      if (missing(column_name)) {
        stop("Le nom de la colonne doit être spécifié")
      }
      # Vérification de l'existence de la colonne
      if (!column_name %in% colnames(self$data)) {
        stop(sprintf("La colonne '%s' n'existe pas", column_name))
      }
      # Extraction des données
      col_data <- self$data[[column_name]]
      # Vérification du type numérique
      if (!is.numeric(col_data)) {
        stop("La colonne doit contenir des données numériques")
      }
      # Calcul des statistiques
      stats <- list(
        "n_observations" = as.integer(length(col_data)),
        "n_manquants" = as.integer(sum(is.na(col_data))),
        "moyenne" = round(mean(col_data, na.rm = TRUE), 2),
        "mediane" = round(median(col_data, na.rm = TRUE), 2),
        "minimum" = round(min(col_data, na.rm = TRUE), 2),
        "maximum" = round(max(col_data, na.rm = TRUE), 2),
        "ecart_type" = round(sd(col_data, na.rm = TRUE), 2),
        "q1" = round(quantile(col_data, 0.25, na.rm = TRUE), 2),
        "q3" = round(quantile(col_data, 0.75, na.rm = TRUE), 2),
        "iqr" = round(IQR(col_data, na.rm = TRUE), 2),
        "variance" = round(var(col_data, na.rm = TRUE), 2),
        "skewness" = round(moments::skewness(col_data, na.rm = TRUE), 2),
        "kurtosis" = round(moments::kurtosis(col_data, na.rm = TRUE), 2)
      )
      # Retour des résultats
      data.frame(
        Statistique = names(stats),
        Valeur = (unlist(as.numeric(stats)))
      )
    }
  )
)

# Exemple d'utilisation
stats <- statistiques$new(
  file_name = "../cleanedData/Data_wtout_na.xlsx",
  sheet_name = "Sheet1"
)

resultat <- stats$get_statistics("DAM")
print(resultat)