#Stray number
def make_list():
    print("Enter number of elements in list:")
    l=int(input())
    list1=[]
    print("Enter elements:")
    for i in range(l):
        list1.append(int(input()))
    print(list1)
    return list1
    


def Stray():
    list1=make_list()
    for i in list1:
        for j in range(len(list1)):
            if i!=list1[j]:
                return "Stray number is:",list1[j]

#Close to its mean

def mean():
    list1=make_list()
    sum=0
    for i in list1:
        sum=sum+i
    avg=sum/len(list1)
    print("Mean is:",avg)
    
    l=[]
    for i in list1:
        if i==avg:
            return "closest number to mean is:",i
        a=i%avg
        l.append(a)
    b=l.index(max(l))

    return "closest no. to mean :",list1[b]

#Number of people inside a bus

def bus():
    print("Enter number of bus stations:")
    n=int(input())
    print("----consider there are already 10 people inside bus----")
    sum=10
    for i in range(1,n+1):
        print("Enter number of people onboarding at station ",i)
        a=int(input())
        print("Enter number of people alighting at station ",i)
        b=int(input())
        sum=sum+a-b
    return "Number of people inside bus is",sum

#Missing number in a list

def Missing():
    print("Enter the original list")
    l1=set(make_list())
    print("Enter modified list")
    l2=set(make_list())

    l3=l1-l2

    return(l3)


#Diff betn 2 lowest no.

def diff_2_low():
    l=make_list()
    l.sort()
    print(l)
    a=l[1]-l[0]
    return a

#No. of elements smaller than their mean

def smaller_mean():
    list1=make_list()
    sum=0
    for i in list1:
        sum=sum+i
    avg=sum/len(list1)
    print("Mean is:",avg)
    count=0
    for i in list1:
        if i<avg:
            count+=1
    return count

#Average Speed

def avg_speed(list1):
    return sum(list1)/len(list1)

