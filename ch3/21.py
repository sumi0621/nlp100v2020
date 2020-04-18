import pandas as pd

df = pd.read_json('ch3/jawiki-country.json.gz', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]

uk_list = uk_text.split('\n')
print(list(filter(lambda x: 'Category:' in x, uk_list)))