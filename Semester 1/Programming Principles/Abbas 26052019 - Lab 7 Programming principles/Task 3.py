direction = input("Enter 'up' or 'down': ")

if direction == "up":
    num = int(input("enter a number higher than 1:"))
    if num > 0: 
          for x in range(0, num):
             print(1+ x)
elif direction == "down":
    num = int(input("enter a number below 50: "))
    count = 50 - num
    for count in range(0, num):
        if num < 50 and num > 0:
         print(50 - count)
else:
    print("I don't understand")





