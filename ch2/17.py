import pandas as pd

df = pd.read_csv("ch2/popular-names.txt", sep="\t", header=None)

data = df[0]

print(data.unique())