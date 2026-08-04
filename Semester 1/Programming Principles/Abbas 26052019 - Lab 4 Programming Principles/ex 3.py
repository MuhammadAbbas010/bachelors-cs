a = int(input("Enter a number (a): "))
b = int(input("Enter a number (b): "))
result = 1
rep = 1 
while rep <= b: 
    result = result * a
    rep = rep + 1 

print(f"{a} to the power of {b} =  {result}")
