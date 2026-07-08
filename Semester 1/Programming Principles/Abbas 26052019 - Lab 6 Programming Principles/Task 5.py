my_list = []
count = 1
data = input("Enter input: ")

while count <= 4:
    my_list.append((data))
    data = input("enter a number: ")
    count += 1

my_list.sort()
index = len(my_list) -1

while index >= 0:
    print(my_list)
    del my_list[index]
    index -= 1





