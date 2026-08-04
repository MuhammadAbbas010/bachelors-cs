import random 
decision = input("would you like to enter the program 'Y' or 'N': ")
score = 0
while decision.upper() == "Y":
    max_temp = int(input("Give max_temp: "))
    min_temp = int(input("Give min_temp: "))
    for x in range(min_temp, max_temp):
     num1 = random.randint(min_temp, max_temp)
     num2 = random.randint(min_temp, max_temp)
    celtoFar = int(input(f"{num1} C * 9/5  = {num1* (9/5)} F"))
    fartoCel = int(input(f"{num2 -32} F * 5/9  = {num1* (5/9)} C"))


    decision = input("Would you like to play again ?  'Y'  or  'N'")