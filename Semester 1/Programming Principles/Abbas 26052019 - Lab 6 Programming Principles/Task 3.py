forward_list = []
count = 1 
data = input("enter a number: ")

while count <= 4:
    forward_list.append(int(data))
    data = input("enter a number: ")
    count += 1

forward_list.sort()
print("The numbers entered are: ", forward_list)

reverse_list = []
index = len(forward_list) - 1

while index >= 0: 
    reverse_list.append(forward_list[index])
    index -= 1

print("the list in reverse is ", reverse_list)


