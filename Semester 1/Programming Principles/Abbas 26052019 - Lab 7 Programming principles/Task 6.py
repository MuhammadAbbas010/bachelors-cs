
def read_number(size):
    user_list = [] * size
    for x in range(0,size):
        number = int(input("Enter a number: "))
        user_list.append(number)

    return user_list


def find_max(list):
    max = list[0]
    for num in list:
            if num > max:
                max = num
    return max


def find_min(list):
    min = list[0]
    for num in list:
            if num < min:
                min = num
    return min



def main():
    print("A program to find the maximum and minimum numbers in a list\n")
    size= int(input("How many numbers do you want the list to be: "))

    my_list = read_number(size)    #double check if I will need the []
    maximum = find_max(my_list)
    minimum = find_min(my_list)

    print(my_list)
    print(f"Maximum number: {minimum}")
    print(f"Minimum number: {maximum}")


main()
