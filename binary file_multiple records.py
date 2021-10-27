'''Code a menu driven program to append, display, search, update
and delete book records in a binary file format
[bno,bname, publisher, price]'''
import pickle
import os

def create_file():
    n=int(input("How many books: "))
    f=open("book.dat","wb")
    for i in range(n):
        t=eval(input("Enter bno,name,publisher and price: "))
        pickle.dump(t,f)
    f.close()


def add_records():
    n=int(input("How many books: "))
    f=open("book.dat","ab")
    for i in range(n):
        t=eval(input("Enter bno,name,publisher and price: "))
        pickle.dump(t,f)
    f.close()

def read_file():
    f=open("book.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            print(d)
    except:
        f.close()

def update_rec():
    f=open("book.dat","rb")
    g=open("t.dat","wb")

    publ=input("Enter name of publisher whose record is to be updated: ")
    try:
        while True:
            d=pickle.load(f)
            if d[2].upper()==publ.upper():
                d[3]+=50
            pickle.dump(d,g)
    except:
        f.close()
        g.close()
    os.remove("book.dat")
    os.rename("t.dat","book.dat")
    
            

       
def remove_rec():
    f=open("book.dat","rb")
    g=open("t.dat","wb")
    nm=input("Enter the name of the publisher whose books have to be removed: ")
    try:
        while True:
            d=pickle.load(f)
            if d[2].upper()!=nm.upper():
                pickle.dump(d,g)
    except:
        f.close()
        g.close()
    os.remove("book.dat")
    os.rename("t.dat","book.dat")
    
            

create_file()
while True:
    choice=int(input("Enter 1 to append, 2 to display, 3 to update, 4 to delete and 5 to exit"))
    if choice==1:
        add_records()
    elif choice==2:
        read_file()
    elif choice==3:
        update_rec()
    elif choice==4:
        remove_rec()
    elif choice==5:
        break
    else:
        print("Invalid choice")
        








'''
def search_record():
    f=open("book.dat","rb")
    count=0
    try:
        while True:
            d=pickle.load(f)
            if d[3]>=500 and d[3]<=1000:
                print(d)
                count+=1
    except:
        f.close()
    if count==0:
        print("No book in the given price range")
    '''    
