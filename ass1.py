#Problem no 1
"""

def biggest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("---THIS IS PROGRAM OF BIGGEST OF 3 NUMBERS---")
print("Enter 3 numbers:")
print("Biggest number is :",biggest(int(input()),int(input()),int(input())))

"""

#Problem no 2
"""

def armstrong(a):
    sum=0
    n=1
    p=a
    while a>0:
        n=a%10
        a=a//10
        sum=sum+(n*n*n)
    a=p
    if sum==a:
        return "It is an armstrong number"
    else:
        return "It is not an armstrong number"
 
print("---THIS IS PROGRAM FOR ARMSTRONG NUMBER---")
print("Enter any number:")
print(armstrong(int(input())))

"""

#Problem no 3
"""
def rev(a):
    return a[::-1]

print("Enter a number you want to reverse")
print(rev(str(input())))

def sum(a):
    sum=0
    n=0
    while a>0:
        n=a%10
        sum=sum+n
        a=a//10
    return sum

print(sum(int(input())))

"""

#Problem no 6 leap year
"""
def leap(a):
    if a%4==0:
        if a%100==0:
            if a%400==0:
                return "It is a leap year"
            else :
                return "It is not a leap year"
        else :
            return "It is a leap year"
    else :
        return "It is not a leap year"

print(leap(int(input())))

"""

#Problem no 7 triangle
"""
def tri(a,b,c):
    if a==b==c:
        return "Equilateral Triangle"
    elif a==b or a==c or b==c:
        return "Isosceles"
    elif a!=b!=c:
        if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            return "Right angled"
        else :
            return "Scelen triangle"
    else :
        return "It is not a triangle"

print("Enter sides of Triangle")
print(tri(int(input()),int(input()),int(input())))

"""

#Problem no 8 quadratic equation
"""

def quad(a,b,c):
    dt=(b*b-4*a*c)
    if dt==0:
        return -b/(2*a),-b/(2*a)
    else:
        return (-b+(dt**0.5))/(2*a),(-b-dt**0.5)/(2*a)

print(quad(int(input()),int(input()),int(input())))

"""

#Problem no 9 quadrant 
"""
def quadrant(a,b):
    if a>0 and b>0:
        return "1st Quadrant"
    elif a<0 and b<0:
        return "3rd Quadrant"
    elif a<0 and b>0:
        return "2nd Quadrant"
    else :
        return "4th Quadrant"

print("x,y lies in :",quadrant(float(input()),float(input())))

"""

#Problem no 10 arithematic
"""

def arithematic(a,b,c):
    if b=="+":
        return a+c
    elif b=="-":
        return a-c
    elif b=="*":
        return a*c
    else :
        return a/c
    
print("Result:",arithematic(float(input()),str(input()),float(input())))
"""

#Problem no 11 fibonacci 
""""
def fibo(a):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(2,a):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
    
fibo(int(input()))

"""
#Problem no 11 tribonacci 
"""
def tribo(a):
    n1=0
    n2=1
    n3=1
    print(n1)
    print(n2)
    print(n3)

    for i in range(3,a):
        n4=n1+n2+n3
        print(n4)
        n1=n2
        n2=n3
        n3=n4

tribo(int(input()))
"""
#Problem no 12 factorial

"""
def fact(a):
    x=1
    for i in range(1,a+1):
        x=x*i
    return x

print(fact(int(input())))
"""
#Problem no 13 factors 
"""
def sum_fact(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum=sum+i
    return sum

print(sum_fact(int(input())))
"""
#Problem no 14 vowel 
"""
def vowel(a):
    l=['a','e','i','o','u']
    if a in l:
        return "Given char is vowel"
    else:
        return "Given char is consonant"

print(vowel(input()))

"""

#Digital roots 



#List of prime numbers for a given range
"""

l=[]
a=int(input())
for i in range(2,a+1):
    for j in range(2,i):
        if i%j==0:
            break
    else :
            l.append(i) 

print(l)
print("Number of prime number in given range are:")
print(len(l))

"""

#Triangular sum

def tri_sum(a):
    b=a*(a+1)*(a+2)/6
    return b

print(tri_sum(int(input())))
