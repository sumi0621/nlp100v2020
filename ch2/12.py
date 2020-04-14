import pandas as pd

df = pd.read_csv("ch2/popular-names.txt", sep="\t", header=None)
df[0].to_csv("col1.txt", index=False, header=None)
df[1].to_csv("col2.txt", index=False, header=None)