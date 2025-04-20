using Statistics, XLSX, DataFrames, HypothesisTests

# Charger les données
df = XLSX.readtable("AAA.xlsx", "Sheet1") |> DataFrame

function safe_anova(df, value_col, group_col)
    # Conversion et nettoyage des données
    df[!, value_col] = convert(Vector{Float64}, df[!, value_col])  # Correction: Vector{Float64} au lieu de Vector(Float64)
    df = dropmissing(df, [value_col, group_col])  # Correction: vérifier les deux colonnes
    
    # Préparation des groupes
    groups = unique(df[!, group_col])
    group_data = [df[!, value_col][df[!, group_col] .== g] for g in groups]
    
    # Vérification qu'on a au moins 2 groupes avec données
    length(groups) < 2 && error("Moins de 2 groupes avec données valides")
    
    # Correction principale: utiliser l'opérateur splat (...) pour passer les groupes séparément
    OneWayANOVATest(group_data...)
end

# Utilisation
test_result = safe_anova(df, "DAM", "Profession_agreg_CM")
println(test_result)