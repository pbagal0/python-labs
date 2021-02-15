#----------------Assignment 3 ----------------
from assignment2 import make_list
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

#Isogram

def isogram(a):
	    return True if len(list(a))==len(set(a)) else False

#Largest number deleting single digit

def Del_dig(x):
    x=list(x)
    z=0
    list1=[]
    list2=[]
    for i in range(len(x)):
	    list2=x.copy()
	    list2.pop(z)
	    list1.append(int("".join(list2)))
	    z+=1
    return max(list1)

#Largest number by shuffling the digit

def largest_num(a):
    count = [0 for x in range(10)]
    string = str(a)
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1
    res = 0
    mul = 1
    for i in range(10):
        while count[i]>0:
            res = res + (i * mul)
            count[i] = count[i] - 1
            mul = mul * 10
    return res

#Accumulated string


def accum(s):
    ans = ''
    i = 0
    while i < len(s):
        n = 0
        while n < i+1:
            if n == 0:
                ans += s[i].upper()
            else:
                ans += s[i].lower()
            n+= 1
        ans += '-'
        i += 1
    return ans[:len(ans)-1]

#RGB to HEX

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % (rgb)

#HEX TO RGB

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

