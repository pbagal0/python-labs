

#Bank Account

class Bank:

    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance

    def debit(self,a):
        self.balance=self.balance-a

    def credit(self,a):
        self.balance=self.balance+a

#Mobile Billing

class Mobile:
    def __init__(self,balance,call_time,no_of_sms):
        self.balance=balance             #main balance
        self.ct=call_time                #time in seconds
        self.no_of_sms=no_of_sms         
        self.charges_call=0.01
        self.charges_sms=1

    def bill(self):
        self.total_charges=self.ct*self.charges_call+self.no_of_sms*self.charges_sms
        self.balance=self.balance-self.total_charges
        return f"Total charges of service are {self.total_charges} & Your remaining balance is {self.balance}"

#Colour

class Colour:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

    def form_colour(self):
        return webcolours.hex_to_name(self.r,self.g,self.b)

#Point

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def quad(self):
        if self.x>0:
            if self.y>0:
                return "1st Quadrant"
            elif self.y<0:
                return "4th Qudrant"
            else:
                return "X axis"
        elif self.x<0:
            if self.y>0:
                return "2nd Quadrant"
            elif self.y<0:
                return "3rd Qudrant"
            else:
                return "X axis"
        elif self.x==0:
            if self.y==0:
                return "Origin"
            else:
                return "Y axis"
    #def __str__(self):
     #   return "Point ({self.x},{self.y} )"
    
    def dis(self):
        return ((self.x**2+self.y**2)**0.5)


#Circle , Triangle , Rectangle

class Circle:
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return 3.14*self.r**2
    
    def circum(self):
        return 2*3.14*self.r

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

        self.s=(self.a+self.b+self.c)/2
    
    def area(self):
        return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5
    
    def perimeter(self):
        return self.a+self.b+self.c

class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def perimeter(self):
        return 2*(self.l+self.b)
    
    def area(self):
        return self.l*self.b


#Box

class Box:
    def __init__(self,length,breadth,height):
        self.l=length
        self.b=breadth
        self.h=height
    
    def display(self):
        return self.l,self.b,self.h

    def volume(self):
        return self.l*self.b*self.h

