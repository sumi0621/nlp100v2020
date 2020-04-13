import random

def exchange_str(string):
    words = string.split(" ")
    ret = ""

    for word in words:
        if len(word) > 4:
            first = word[0]
            last = word[-1]
            listed_word = [i for i in word]
            listed_word = listed_word[1:-1]
            random.shuffle(listed_word)
            word_ex = first + "".join(listed_word) + last
            ret += word_ex + " "
        else:
            ret += word + " "
    return ret

string = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(exchange_str(string))