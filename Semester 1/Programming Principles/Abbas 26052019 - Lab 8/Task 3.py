from random import randint

def add():
    num1 = randint(5,20)
    num2 = randint(5,20)
    userGuess = int(input(f"Enter the sum of {num1} + {num2} \n: "))
    return userGuess, (num1+num2)

def sub():
    num1 = randint(25,50)
    num2 = randint(1,25)
    userGuess = int(input(f"Enter the result of {num1} - {num2} \n: "))
    return userGuess, (num1 - num2)



def equalOrNot(user, computer):
    if user == computer:
        print("Your answer is correct")
    else: 
        print(f"Your answer is incorrect. the correct answer is {computer}")
        


def main():
    while True:
        selection = int(input("Enter a number based on your seleection\n1. Addition\n2.Subtraction\nInput: "))
        if selection == 1:
            userAdd, addAnswer = add()
            equalOrNot(userAdd, addAnswer)
            break
        elif selection ==2:
            userSub, subAnswer = sub()
            equalOrNot(userSub, subAnswer)
            break
        else: 
            print("Invalid input, please try again.")

main()