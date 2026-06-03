from selectors import SelectSelector

selection = input("Enter 'C' or 'c' for circle and 'R' or 'r' for rectangle: ")

if selection.upper() == "C":
    print("Area = 3.14 * radius^2")
    radius = float(input("Enter the radius of the circle: "))
    print(f"Area = 3.14 * radius^2 = {radius*radius * 3.14}")
elif selection.upper() == "R":
    print("Area = length * width")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area = length * width = {length * width}")
else:
    print("Only choose between the options 'C' or 'R'")


