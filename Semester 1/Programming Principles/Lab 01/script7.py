hourlyWage = float(input("Enter the hourly wage ($): "))
totalHours = float(input("Enter the total hours: "))
totalOvt = float(input("Enter the total overtime volume: "))

reg = hourlyWage * totalHours
ovt = hourlyWage * totalHours * 1.5
total = ovt + reg
print(f"Your total pay is equals to {total}($)")
