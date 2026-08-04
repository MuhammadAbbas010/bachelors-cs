import math

r = float(input("Enter the radius of your circle: "))

D = 2* r
circumference = 2*  math.pi *r
surfaceArea = 4* math.pi * (r*r)
volume = math.pi * (r*r*r) * (4/3)

print(f"The volume of your object is = {volume}, its circumference is = {circumference}, \nand its surface area is = {surfaceArea} and its volume is = {volume}")
