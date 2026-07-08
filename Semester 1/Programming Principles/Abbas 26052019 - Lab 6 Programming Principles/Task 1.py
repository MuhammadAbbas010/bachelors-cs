print("The program automatically ends when you type in the word 'stop':")
data = input("Enter a number: ")

my_list = []
while data != "stop":
    my_list.append(int(data))
    data = input("Enter a number: ")

my_list.sort()
print("The numbers you entered are:", my_list)
