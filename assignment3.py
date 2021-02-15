#----------------Assignment 3 ----------------
from ass2 import make_list
#IP address to integer

def ip(a):
    s=a.split('.')
    l=[]
    for i in s:
        l.append(int(i))
    print("The inter for ip address is:")
    return l

def integer():
    l=make_list()
    list1=[]
    for i in l:
        list1.append(str(i))
    print(list1)
    x='.'.join(list1)
    print("The ip address for integer is :")
    return x


#Mexican Wave

def wave(a):
    l=[]
    for i,j in enumerate(a[:]):
        u=a[i].upper()
        b=a[:i]+u+a[i+1:]
        l.append(b)
    print("The mexican wave:")
    return l

#Word frequency

def frequency(a):
    
    l=a.split(" ")
    print(l)

    for i in l:
        count=0
        for j in l:
            if i==j:
                count+=1
        print("Frequency of",i,"is:",count)

#Malformed time

def time(a):

    l=a.split(":")
    l1=[]
    for i in l:
        l1.append(int(i))
    

    if l1[2]>60:
        l1[1]=l1[1]+1
        l1[2]=l1[2]-60
    
    if l1[1]>60:
        l1[0]=l1[0]+1
        l1[1]=l1[1]-60
    
    l2=[]
    for i in l1:
        l2.append(str(i))
    
    return ":".join(l2)

#Malformed date

def date(a):

    l=a.split("/")
    l1=[]
    for i in l:
        l1.append(int(i))
    

    if l1[0]>31:
        l1[1]=l1[1]+1
        l1[0]=l1[0]-31
    
    if l1[1]>12:
        l1[2]=l1[2]+1
        l1[1]=l1[1]-12
    
    l2=[]
    for i in l1:
        l2.append(str(i))
    
    return "/".join(l2)

