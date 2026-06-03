from selectors import SelectSelector
dayNum = 0
#while dayNum <1 or dayNum > 7:
dayNum = int(input("Enter the day (1 - 7): "))

    # if dayNum < 1 or dayNum > 7:
    #   print("Please input a number between 1 and 7 ")

match dayNum:
    case  1:
        print("Peppermint mocha")
    case 2:
        print("Candy bar latte")
    case 3:
        print("Caramel coffee")
    case 4:
        print("Chocolate almond cafe au lait")
    case 5:
        print("Pumpkin-chai latte")
    case 6:
        print("Vanilla chai tea")
    case 7:
        print("Gingerbread latte")
    case _:
        print("Please input a number between 1 and 7 ")



