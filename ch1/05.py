def char_bi_gram(string):
    if string is list:
        string = "".join(string)
    
    string = string.replace(" ", "")
    bigram = []
    for i in range(0, len(string) - 1):
        bigram.append(string[i:i+2])
    
    return bigram

def word_bi_gram(string):
    if string is list:
        string = "".join(string)
    
    bigram = []

    words = string.split(" ")

    for i in range(0, len(words) - 1):
        bigram.append(words[i] + words[i + 1])
    
    return bigram

string = "I am an NLPer"
print(char_bi_gram(string))
print(word_bi_gram(string))