annual_salary = float(input("Enter your annual salary: "))
tax = 0
if annual_salary <= 2500:
    tax = 0
elif annual_salary > 2501 and annual_salary <= 10000:
        tax = 0.05
elif annual_salary > 10001 and annual_salary <= 50000:
        tax = 0.15
elif annual_salary > 50001:
        tax = 0.25

print(f"Your salary gets {round((annual_salary*tax),2)}MYR deducted from every year, leaving you with take home of {((1-tax)*annual_salary),2}MYR")


