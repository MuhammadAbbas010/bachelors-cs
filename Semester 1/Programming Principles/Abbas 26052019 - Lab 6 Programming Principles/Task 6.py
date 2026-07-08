my_list = []
count = 1
data = input("Enter input: ")

while count <= 4:
    my_list.append((data))
    data = input("enter a number: ")
    count += 1

my_list.sort()
index = len(my_list) -1


print(my_list)
while index >= 0:
    if index %2 == 0:
        del my_list[index]
        print(my_list)
    index -= 1





