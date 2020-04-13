string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = string.split(" ")

first_words_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

d = dict()
for i, word in enumerate(words):
    if i in first_words_index:
        d[words[i][0]] = 0
    else:
        d[words[i][1]] = 1

print(d)