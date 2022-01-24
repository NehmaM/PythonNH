# Create a Rectangle class with attributes length and breadth and methods to find area
#and perimeter. Compare two Rectangle objects by their area.

class Rectangle():

    def __init__(self,leng,bdt):
        self.length = leng
        self.breadth = bdt

    def area(self):
        return(self.length*self.breadth)

    def peri(self):
        return(2*(self.length*self.breadth))


a=int(input("Enter length of rectangle for object1: "))
b=int(input("Enter breadth of rectangle for object1: "))

c=int(input("Enter length of rectangle for object2: "))
d=int(input("Enter breadth of rectangle for object2: "))

obj1 = Rectangle(a,b)
obj2 = Rectangle(c,d)

area1 = obj1.area()
area2 = obj2.area()

if(area1 == area2):
    print(f"Area of object1 {area1} is equal to area of object2 {area2}")
else:
    print(f"Area of object1 {area1} is not equal to area of object2 {area2}")
