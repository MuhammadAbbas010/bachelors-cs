data = int(input("Enter how many gigabytes of data you would like to purchase: "))
charge = 0
if data <= 10:
    charge = data* 15
elif data > 10:
    charge = (data - 10) * 30 + (10 * 15)

print(f"Your charge is RM {charge}")

