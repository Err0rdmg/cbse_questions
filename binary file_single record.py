#write a menu driven program to append,search,delete and display operations on binaryfile 'student' containing admission number name and percentage of the student. the search and delete operation should be on the basis of admission number
import pickle
import os
def create_file():
    f=open('school','wb')
    n=int(input('Enter number of students :'))
    data=[]
    for i in range(1,n+1):
        s_data=eval(input('Enter admission number, name and percentage of student '+str(i)+' :'))
        data.append(s_data)
    pickle.dump(data,f)
    f.close()
    
def append():
    f=open('school','rb+')
    data=pickle.load(f)
    s_data = eval(input('Enter admission number, name and percentage of student :'))
    f.seek(0)
    data.append(s_data)
    pickle.dump(data,f)
    f.close()

    
def search():
    f=open('school','rb')
    n=int(input('Enter admission number of student to be searched :'))
    print('SEARCHING FOR CONTENTS OF STUDENT ON BASIS OF ADMISSION NUMBER')
    count=0
    data=pickle.load(f)
    for i in data:
        for j in i:
            if j==n:
                print(i)
                count=1
    if count==0:
        print('Student not found')
    f.close()
def delete():
    f=open('school','rb')
    g=open('temp','wb')
    o_rec=pickle.load(f)
    n_rec=[]
    count=0
    n=int(input('Enter admission number of student to be removed :'))
    for i in o_rec:
        if i[1]!=n:
            n_rec.append(i)
        else:
            count=1
    pickle.dump(n_rec,g)
    if count==1:
        print('RECORD FOUND AND REMOVED')
    f.close()
    g.close()
    os.remove('student')
    os.rename('temp','student')
def display():
    f=open('school','rb')
    print('DISPLAYING CONTENTS OF STUDENT FILE')
    rec=pickle.load(f)
    print(rec)
    f.close()
print('CREATING FILE')
create_file()
print('Enter 1 to append record\nEnter 2 to Search Record\nEnter 3 to delete record\nEnter 4 to display record')
while True:
    n=int(input('Enter Your Choice :'))
    if n==1:
        append()
    elif n==2:
        search()
    elif n==3:
        delete()
    elif n==4:
        display()
    else:
        print('INVALID INPUT')
        break


