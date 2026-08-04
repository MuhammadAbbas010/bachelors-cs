
print("[1] Create a new file\n[2] Display the file\n[3] Add a new item to the file")
choice = int(input("Enter 1, 2 or 3 \n:"))

if choice == 1:
    subj = input("Enter a subject name: ")
    file = open("Subjects.txt", 'w')
    file.write(subj + '\n')
    file.close()
        
elif choice == 2: 
    file = open("Subjects.txt", 'r')
    for line in file: 
        print(line)
    file.close()
elif choice == 3: 
    file = open ("Subjects.txt", 'a')

    subj2 = input("Enter a subject: ")
    file.write(subj2  + '\n')

    file.close()
else:
    print("Only options 1-3 are allowed")






