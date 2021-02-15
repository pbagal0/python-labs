#Problem no 1


def biggest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c



#Problem no 2

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
 




#Problem no 3

def rev(a):
    a=str(a)
    return a[::-1]

def sum(a):
    sum=0
    n=0
    while a>0:
        n=a%10
        sum=sum+n
        a=a//10
    return sum


#Problem no 6 leap year

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



#Problem no 7 triangle

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



#Problem no 8 quadratic equation

def quad(a,b,c):
    dt=(b*b-4*a*c)
    if dt==0:
        return -b/(2*a),-b/(2*a)
    else:
        return (-b+(dt**0.5))/(2*a),(-b-dt**0.5)/(2*a)


#Problem no 9 quadrant 

def quadrant(a,b):
    if a>0 and b>0:
        return "1st Quadrant"
    elif a<0 and b<0:
        return "3rd Quadrant"
    elif a<0 and b>0:
        return "2nd Quadrant"
    else :
        return "4th Quadrant"


#Problem no 10 arithematic

def arithematic(a,b,c):
    if b=="+":
        return a+c
    elif b=="-":
        return a-c
    elif b=="*":
        return a*c
    else :
        return a/c
    

#Problem no 11 fibonacci 

def fibo(a):
    n1=0
    n2=1
    l=[0,1]
    for i in range(2,a):
        n3=n1+n2
        l.append(n3)
        n1=n2
        n2=n3
    return l


#Problem no 11 tribonacci 

def tribo(a):
    n1=0
    n2=1
    n3=1
    l=[0,1,1]

    for i in range(3,a):
        n4=n1+n2+n3
        l.append(n4)
        n1=n2
        n2=n3
        n3=n4
    return l


#Problem no 12 factorial

def fact(a):
    x=1
    for i in range(1,a+1):
        x=x*i
    return x


#Problem no 13 factors 

def sum_fact(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum=sum+i
    return sum


#Problem no 14 vowel 

def vowel(a):
    l=['a','e','i','o','u']
    if a in l:
        return "Given char is vowel"
    else:
        return "Given char is consonant"

#Digital roots 

def digitalRoot(num): 
      
    if (num == "0"): 
        return 0
    ans = 0
    for i in range (0, len(num)): 
        ans = (ans + int(num[i])) % 9
          
    if(ans == 0): 
        return 9
    else:  
        return ans % 9

#Prime number

def prime(b,a):
    l=[]
    for i in range(b,a+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
    return l,"number of prime no.:",len(l)


#Triangular sum

def tri_sum(a):
    b=a*(a+1)*(a+2)/6
    return b


#NCR

def NCR(n):
    return(fact(n)//(fact(2)*fact(n-2)))



