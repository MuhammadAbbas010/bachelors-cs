bill = float(input("What is your bill?\n: "))

serviceCharge = 1.1
GST = 1.06
total = (bill * serviceCharge)*GST
Friends = int(input("How many friends do you have?\n: "))

print(f"Your grand total is = {round(total, 3)}, divided amongst your {Friends} friends it would be {round(total/Friends, 2)} ")