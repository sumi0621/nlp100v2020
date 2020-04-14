with open("ch2/popular-names.txt", "r") as f:
    string = f.read()
    print(string.count("\n"))
