num = int(input("enter a number between 1 and 12: "))

for x in range(1,13):

    if num < 12 and num > 0:
        print(f"{num} x {x} = {num * x}")
