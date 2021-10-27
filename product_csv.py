import csv
import os
def write_data():
    f=open("product.csv","w") 
    w=csv.writer(f,delimiter=',',lineterminator='\n') 
    w.writerow(["Product Id", "Product name","Cost"]) 
    w.writerow(["P1","TV", 20000] ) 
    w.writerow(["P2","LAPTOP", 50000] ) 
    w.writerow(["P3","WASHING MACHINE", 50000] )
    f.close()
def display_max():
    f=open("product.csv","r")
    rec=csv.reader(f)
    print("Details of products with maximum cost") 
    next(rec)
    Val=[]
    for i in rec:
        Val.append(float(i[2])) 
    m=max(Val)
    print(m)
    f.seek(0)
    next(rec) 
    print("Result")
    for i in rec:
        if float(i[2])==m:
            print(i) 
    f.close()
def append():
    f = open("product.csv","a")
    w = csv.writer(f)
    n = int(input("Enter the number of items you want to add to the csv file: "))
    count = 1
    for i in range(n):
        id = input("Enter the product {count} id: ".format(count = count))
        name=input("Enter product {count} name: ".format(count = count)) 
        cost=float(input("Enter cost of the {count} product: ".format(count = count)))
        data = [id, name, cost]
        w.writerow(data)
        count += 1
    f.close()
def remove_data():
    f = open("product.csv", "r")
    g = open("temp.csv", "w")
    w = csv.writer(g)
    nme = input("Enter the name of the product you want to delete:")
    red = csv.reader(f)
    header = next(red)
    w.writerow(header)
    for i in red:
        if i[1].lower()!= nme.lower():
            w.writerow(i)
    f.close()
    g.close()
    os.remove("product.csv")    
    os.rename("temp.csv","product.csv")

def update_cost():
    f = open("product.csv",'r')
    g = open("temp.csv","w")
    w = csv.writer(g)
    nme = input("Enter the name of the product you want to update the cost for:")
    red = csv.reader(f)
    header = next(red)
    w.writerow(header)

    for i in red:
        if i[1].lower()== nme.lower():
            i[2] = float(input("Enter the cost you want to update:"))
        w.writerow(i)
    f.close()
    g.close()
    os.remove("product.csv")
    os.rename("temp.csv","product.csv")

def menu():
    try:
        men = input("Enter w to write, dm to display the products with maximum cost, a to append, uc to update cost and rd to remove data in the csv file: ")
        if men.lower() =="w":
            write_data()
        if men.lower() == "dm":
            display_max()
        if men.lower() == "a":
            append()
        if men.lower() == "uc":
            update_cost()
        if men.lower() == "rd":
            remove_data()
    except:
        print("Sorry there was some problem, Please try again :( ")
# write_data()
# display()
# append()
# remove_data()
# update_cost()
menu()