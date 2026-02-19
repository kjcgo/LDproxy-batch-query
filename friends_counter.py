import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("modified_query_snp_list_2.0.csv")
friend_count = []
var = []

counts = df["#"]
ids = df["query"]

for i in range(1, counts.size):
    if int(counts[i]) == 1:
        #print(i, ids[i-1])
        friend_count.append(counts[i-1])
        var.append(ids[i-1])

friend_count.append(df.iloc[-1, 0])
var.append(df.iloc[-1,1])

df = pd.DataFrame({
    "Lead SNP": var,
    "# of LD Variants": friend_count,
})

hist = df.hist(column = "# of LD Variants", bins = 100)
df.to_csv("friend_count.csv", index=False)
plt.savefig("friend_count.png")
plt.show()

