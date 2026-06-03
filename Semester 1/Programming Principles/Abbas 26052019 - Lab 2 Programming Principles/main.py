old = int(input("Input the number of oldies movies you would like to rent: "))
new = int(input("Input the number of new movies you would like to rent: "))

new_charge = new *3
old_charge = old *2

total = old_charge + new_charge

print(f"The total for your new movies would be {new_charge}$ for one nigth")
print(f"THe total for your old movies would be {old_charge}$ for one nigth")
print(f"The total for your new movies would be {round(total,2)}$")

