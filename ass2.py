#Stray number

def Stray():
    print("Enter number of elements in list:")
    l=int(input())
    list1=[]
    for i in range(l):
        list1.append(int(input()))
    
    print(list1)

    for i in list1:
        for j in range(l):
            if i!=list1[j]:
                return list1[j]

s


