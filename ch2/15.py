import pandas as pd

df = pd.read_csv("ch2/popular-names.txt", sep="\t", header=None)

num = int(input())

for i in range(len(df) // num):
    print(df[num*i:num*i + num])