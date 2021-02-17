import math
class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        global s
        s=(self.a+self.b+self.c)/2
        print(s)
    def area(self):
        global s
        d=s*(s-self.a)*(s-self.b)*(s-self.c)
        area=math.sqrt(d)
        print(area)
t1=triangle(3,3,2)
t1.perimeter()
t1.area()
