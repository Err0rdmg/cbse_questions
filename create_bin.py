import pickle 
def write_bin():
    f = open("test","wb")
    we = "The quick brown fox jumps over the lazy dog"
    g = pickle.dump(we,f)
    f.close()
    return g

def read_bin():
    f = open("test","rb")
    l = pickle.load(f)
    print(l)
    f.close()

def write_txt():
    f = open("test.txt","wt")
    # g = f.readlines()
    f.write("The quick brown fox jumps over the lazy dog")
    f.close()

def read_txt():
    f = open("test.txt","rt")
    g = f.read()
    print(g)
    f.close()
    
read_txt()