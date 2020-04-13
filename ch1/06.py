def char_bi_gram(string):
    if string is list:
        string = "".join(string)
    
    string = string.replace(" ", "")
    bigram = []
    for i in range(0, len(string) - 1):
        bigram.append(string[i:i+2])
    
    return bigram

str1 = "paraparaparadise"
str2 = "paragraph"

char1 = set(char_bi_gram(str1))
char2 = set(char_bi_gram(str2))

set0 = set.union(char1, char2) # 和集合
set1 = set.difference(char1, char2) # 差集合
set2 = set.intersection(char1, char2) # 積集合

print(set0)
print(set1)
print(set2)