import pandas as pd

#reduce size of csv
df = pd.read_csv("query_snp_list.csv", low_memory=False)
df_subset = df.iloc[:, [0, 1, 2, 3, 8]]
df_subset.columns = ["#", "query", "rs_number", "coord", "r^2"]

#convert numbering and r^2 columns to numeric types
df_subset['#'] = pd.to_numeric(df_subset['#'], errors='coerce')
df_subset['r^2'] = pd.to_numeric(df_subset['r^2'], errors='coerce')
df_subset = df_subset.dropna(subset=["#", "r^2"])

#bound r^2 values
df_subset = df_subset[df_subset['r^2'] >= 0.1]
df_subset.to_csv("modified_query_snp_list.csv", index=False)
