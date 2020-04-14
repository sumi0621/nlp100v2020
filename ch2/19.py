import pandas as pd

df = pd.read_csv("ch2/popular-names.txt", sep="\t", header=None)

print(df[0].value_counts())