#lambda functions to find area of square, rectangle and triangle

SquareArea = lambda a: a*a
RectArea = lambda l,br:l*br
TgleArea = lambda b,h : (1/2)*b*h

print("Area of square(10):",SquareArea(10))
print("Area of Rectangle(10):",RectArea(10,15))
print("Area of triangle(2,3):",TgleArea(2,3))

