import random 

score = 0
for x in range(0,5):
    num1 = random.randint(0,20)
    num2 = random.randint(0,20)
    answer = int(input(f"{num1} +  {num2} = ?  "))
    if answer == (num1 + num2):
        print("Correct!")
        score += 1
    else: 
        print(f"Wrong, the answer is {num1 + num2}")


print(F"you completed the quiz with a score of {score}")
    