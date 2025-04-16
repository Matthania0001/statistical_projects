using DataFrames
using XLSX
using HypothesisTests

# Définir une classe pour les tests de normalité
struct NormalityTests
    file_path::String
    sheet_name::String
    df::DataFrame
end

# Méthodes associées à la classe
function NormalityTests(file_path::String, sheet_name::String)
    # Charger les données depuis le fichier Excel
    df = DataFrame(XLSX.readtable(file_path, sheet_name))
    return NormalityTests(file_path, sheet_name, df)
end

function check_column_exists(nt::NormalityTests, column_name::String)
    # Vérifier si une colonne existe dans le DataFrame
    if !(column_name in names(nt.df))
        #println("La colonne '$column_name' n'existe pas dans le fichier Excel.")
        return false
    else
        #println("La colonne '$column_name' existe dans le fichier Excel.")
        return true
    end
end

function clean_column(nt::NormalityTests, column_name::String)
    # Supprimer les valeurs manquantes et convertir en Float64
    df = dropmissing(nt.df, column_name)
    if check_column_exists(nt, column_name) == false
        error("La colonne '$column_name' n'existe pas dans le fichier Excel.")
    else
        return df
    end
end

function jarque_bera_test(nt::NormalityTests, column_name::String)
    # Effectuer le test de Jarque-Bera
    df_cleaned = clean_column(nt, column_name)
    jb_test = JarqueBeraTest(Float64.(df_cleaned[!, column_name]))
    println(jb_test)
end

function shapiro_wilk_test(nt::NormalityTests, column_name::String)
    df_cleaned = clean_column(nt, column_name)
    sw_test = ShapiroWilkTest(Float64.(df_cleaned[!, column_name]))
    println(sw_test)
end
# --------------------------------------------------
# Exemple d'utilisation
# --------------------------------------------------

# Instancier l'objet NormalityTests
nt = NormalityTests("../cleanedData/Data_wtout_na.xlsx", "Sheet1")

# Effectuer les tests de normalité sur la colonne 'DAM'
println(jarque_bera_test(nt, "DAM"))
println(shapiro_wilk_test(nt, "DAM"))