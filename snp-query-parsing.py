import pandas as pd

#convert to csv
raw = pd.read_csv("/Users/keeshago/combined_query_snp_list_grch37.txt", sep=r"\s+", engine="python", index_col=False, header=None)
raw.to_csv("combined_query_2.0.csv", index=False)

#reduce size of csv
df = pd.read_csv("combined_query_2.0.csv", low_memory=False)
df_subset = df.iloc[:, [0, 1, 2, 3, 8]]
df_subset.columns = ["#", "query", "rs_number", "coord", "r^2"]

#convert numbering and r^2 columns to numeric types
df_subset['#'] = pd.to_numeric(df_subset['#'], errors='coerce')
df_subset['r^2'] = pd.to_numeric(df_subset['r^2'], errors='coerce')

df_subset = df_subset.dropna(subset=["#", "r^2"])
df_subset = df_subset[df_subset['r^2'] >= 0.1]

#save
df_subset.to_csv("modified_query_snp_list_2.0.csv", index=False)