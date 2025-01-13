import pandas as pd
tsv_file = "programs/prot_on-1.1/results/fold_p01116_o00459_model_0_chain_A_EvoEF1_output/fold_p01116_o00459_model_0_chain_A_proton_scores.tsv"
output_csv = "programs/prot_on-1.1/results/fold_p01116_o00459_model_0_chain_A_EvoEF1_output/summary.analysecomplex.csv"
df = pd.read_csv(tsv_file, sep="\t")
df["mutation"] = df["Positions"] + df["Mutations"]
required_columns = ["Positions", "Mutations", "EvoEF1_Mutant_Scores", "EvoEF1_WT_Scores", "DDG_EvoEF1_Scores"]
if not all(col in df.columns for col in required_columns):
    print(f"Faltan columnas en el archivo. Columnas disponibles: {df.columns}")
else:
    df_csv = df[[
        "mutation", 
        "EvoEF1_Mutant_Scores", 
        "EvoEF1_WT_Scores", 
        "DDG_EvoEF1_Scores"
    ]].rename(columns={
        "EvoEF1_Mutant_Scores": "interactionenergy_mut",
        "EvoEF1_WT_Scores": "interactionenergy_wt",
        "DDG_EvoEF1_Scores": "interactionenergy_delta"
    })
    df_csv.to_csv(output_csv, index=False)

    print(f"File succesfully generated: {output_csv}")
