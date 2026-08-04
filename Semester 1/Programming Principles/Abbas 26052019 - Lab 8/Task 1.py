def get_number():
    num = int(input("Enter a number: "))
    return num

def count_up(num):
    for x in range(1, num + 1):
        print(x)

def main():
    num = get_number()
    count_up(num)

main()