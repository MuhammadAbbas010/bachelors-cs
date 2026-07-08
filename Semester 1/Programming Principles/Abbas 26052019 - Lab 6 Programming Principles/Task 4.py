my_list = []
count = 1
data = input("Enter a number: ")

while count <= 4:
    my_list.append(int(data))
    data = input("enter a number: ")
    count += 1

my_list.sort()
index = len(my_list) -1

while index >= 0:
    del my_list[index]
    index -= 1
    print(my_list)





