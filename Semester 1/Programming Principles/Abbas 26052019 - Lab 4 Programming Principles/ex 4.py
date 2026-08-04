num = input("Enter a number or type 'DONE' to quit: ")
if num != "DONE":
    num = int(num)
result = 0
while num != "DONE":
    result += int(num)
    num = input("Enter a number or type 'DONE' to quit: ")
    if num != "DONE":
        num = int(num)
    

if num == "DONE":
    print(f"The sum of the numbers you entered is: {result}")