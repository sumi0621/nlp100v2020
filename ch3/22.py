import pandas as pd

df = pd.read_json('ch3/jawiki-country.json.gz', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]

uk_list = uk_text.split('\n')
category_list = list(filter(lambda x: 'Category:' in x, uk_list))

category_name = []

for category in category_list:
    s = category.replace('[[', '')
    s = s.replace('|*', '')
    s = s.replace(']]', '')
    s = s.replace('Category:', '')
    category_name.append(s)

print(category_name)