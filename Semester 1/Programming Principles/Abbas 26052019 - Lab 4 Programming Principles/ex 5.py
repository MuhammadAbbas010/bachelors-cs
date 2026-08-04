sNum = 50 
guess = float(input("Guess a number between 1 and 100: "))
attempt = 1 
while guess != sNum:
    attempt += 1
    if guess < sNum:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    guess = float(input("Guess a number between 1 and 100: "))


if guess == sNum: 
    print(f"Congratulations! You guessed the number in {attempt} tries.")