from random import randint 

def low_and_high():
    low = int(input("Enter a small number: "))
    high = int(input("Enter a bigger number: "))

    comp_num = randint(low,high)
    return comp_num 

def get_guess():
    print("\nI am thinking of a number: ")
    guess = int(input("Enter your guess here: : "))
    return guess

def equalOrNot(comp_num, guess):
    while True: 
        if guess > comp_num:
            print("Your guess is greater than comp number, try again")
            guess = get_guess()
            # double check 
        elif guess < comp_num:
            print("Your guess is lower than comp number, try again")
            guess = get_guess()
        else:
             print("You guessed it!")
             break


def main():
    rand_num = low_and_high()
    user_guess = get_guess()
    equalOrNot(rand_num, user_guess)


main()

