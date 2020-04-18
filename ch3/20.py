import pandas as pd

df = pd.read_json("ch3/jawiki-country.json.gz",lines=True)
uk_text = df[df.title == "イギリス"].values[0]
print(uk_text)