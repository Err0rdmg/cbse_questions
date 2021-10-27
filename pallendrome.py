def read_data():
    f = open("test.txt")
    s = f.readlines()
    g = open("text.txt",'wt')
    # for word in s:
    #     wordlist=word.split()
    # print(wordlist)
    # for pallen in wordlist:
    #     x = pallen.strip()
    #     if x == x[::-1]:
    #         x = x + '\n'
    #         g.write(x)
    for line in s:
        x = line.strip()
        if x == x[::-1]:
            print(x,"The line is an pallendrome")
        else:
            print(x,"The line is not pallendrome")

read_data()