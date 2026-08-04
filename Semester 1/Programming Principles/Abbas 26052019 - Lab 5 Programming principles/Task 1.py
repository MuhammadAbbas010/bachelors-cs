import random 

play_again = 'Y'
sNum = random.randint(1,100)
while play_again == 'Y':
    guess = float(input("Guess a number between 1 and 100: "))
    attempt = 1 
    if guess != sNum:
        attempt += 1
        if guess < sNum:
         print("Too low, try again.")
        else:
         print("Too high, try again.")
    if guess == sNum: 
        print(f"Congratulations! You guessed the number in {attempt} tries.")
        print("Would you like to play again?")
        play_again = input().upper()
