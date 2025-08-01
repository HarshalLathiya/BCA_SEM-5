import math

r = float(input("Enter radius of circle: "))
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
s = float(input("Enter side of square: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

print("Area of Circle:", math.pi * r * r)
print("Area of Rectangle:", l * b)
print("Area of Square:", s * s)
print("Area of Triangle:", 0.5 * base * height)
