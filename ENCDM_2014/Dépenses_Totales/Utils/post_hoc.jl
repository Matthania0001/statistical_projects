using Statistics, XLSX, DataFrames, HypothesisTests, Combinatorics

# Charger les données
df = XLSX.readtable("AAA.xlsx", "Sheet1") |> DataFrame

function posthoc_pairwise_ttests(df::DataFrame, value_col::Symbol, group_col::Symbol)
    # Nettoyage des données
    df = dropmissing(df, [value_col, group_col])
    df[!, value_col] = convert(Vector{Float64}, df[!, value_col])

    # Obtenir les groupes uniques
    groups = unique(df[!, group_col])
    n_groups = length(groups)

    # Générer toutes les paires de groupes
    group_pairs = collect(combinations(groups, 2))

    # Nombre total de comparaisons
    m = length(group_pairs)

    # Stocker les résultats
    results = DataFrame(Group1 = String[], Group2 = String[], 
                        t_statistic = Float64[], p_value = Float64[], 
                        p_value_corrected = Float64[])

    for (g1, g2) in group_pairs
        data1 = df[df[!, group_col] .== g1, value_col]
        data2 = df[df[!, group_col] .== g2, value_col]

        # Effectuer le test t
        test = EqualVarianceTTest(data1, data2)
        p_val = pvalue(test)

        # Correction de Bonferroni
        p_val_corrected = min(p_val * m, 1.0)

        # Ajouter les résultats
        push!(results, (string(g1), string(g2), test.t, p_val, p_val_corrected))
    end

    return results
end

# Utilisation
results = posthoc_pairwise_ttests(df, :DAM, :Profession_agreg_CM)
# XLSX.writetable("post-hoc.xlsx", collect(eachcol(results)), names(results))
println(results)
