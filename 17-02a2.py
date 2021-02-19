#complex number

class complex:
    def __init__(self,real,imaginary):
        self.r=real
        self.i=imaginary
    
    def __str__(self):
        return f"({self.r},{self.i})"
    
    def __add__(self,other):
        r=self.r+other.r
        i=self.i+other.i
        return complex(r,i)
    
    def __sub__(self,other):
        r=self.r-other.r
        i=self.i-other.i
        return complex(r,i)
    
    def __mul__(self,other):
        r=self.r*other.r
        i=self.i*other.i
        return complex(r,i)

    def __eq__(self,other):
        if self.r==other.r and self.i==other.i:
            return True
        else :
            return False
    
    def mod(self):
        return (((self.r)**2)+((self.i)**2))**0.5

    def __le__(self,other):
        if self.mod()<=other.mod():
            return True
        else:
            return False
    
    def __ge__(self,other):
        if self.mod()>=other.mod():
            return True
        else:
            return False
"""
c1=complex(5,6)
c2=complex(2,3)
print(c1+c2)
print(c1-c2)
print(c1*c2)

c3=complex(7,9)
print(c1+c2==c3)

print(c1<=c3)

print(c1>=c3)
"""

#Time 

class Time:
    def __init__(self, hh, mm, ss):
       self.hh = hh
       self.mm = mm
       self.ss = ss

       if self.ss > 59:
           self.mm = self.mm + (self.ss//60)
           self.ss = self.ss%60
       if self.mm > 59:
           self.hh = self.hh + (self.mm//60)
           self.mm = self.mm%60


    def __str__(self):
        return f"{self.hh}:{self.mm}:{self.ss}"

    def __add__(self, other):
        h = self.hh + other.hh
        m = self.mm + other.mm
        s = self.ss + other.ss
        return Time(h, m, s)

    def __eq__(self, other):
        if self.hh == other.hh and self.mm == other.mm and self.ss == other.ss:
            return True
        else:
            return False

    def __le__(self, other):
        if self.hh <= other.hh:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.hh > other.hh:
            return True
        else:
            return False
  """          
t1 = Time(10, 73, 64)
t2 = Time(11, 31, 1)

print(t1+t2)

print(t1 == t1)

print(t1 <= t2)
"""
#Currency
#--------------------pylinted-------------
"""this is class"""


class Currency:
    """this is a string"""

    def __init__(self, rupee, paisa):
        self.rupee = rupee
        self.paisa = paisa
        if self.paisa > 99:
            self.rupee += self.paisa//100
            self.paisa = self.paisa % 100

    def __str__(self):
        return f"Rs,{self.rupee}.{self.paisa}"

    def __add__(self, other):
        return Currency(self.rupee + other.rupee, self.paisa + other.paisa)

    def __mul__(self, other):
        return Currency(self.rupee * other.rupee, self.paisa * other.paisa)

    def __le__(self, other):
        if self.rupee <= other.rupee:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rupee > other.rupee:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.rupee == other.rupee and self.paisa == other.paisa:
            return True
        else:
            return False
"""
C1 = Currency(13, 19)
C2 = Currency(8, 519)
print(C1)
print(C2)
print(C1 + C2)
print(C1 * C2)

print(C1 > C2)
"""