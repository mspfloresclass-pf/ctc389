#Patricia Flores
#Create a list of 5 strings with each string being a student name
#Print out your List
#Display a menu with three options. Each option will have anumber the user can choose from.
#The first option will say "Add a Student to the list"
#The Second option will say "Modify student name"
#The third option will say "Remove Student"

students = ["Patty","Miguel","John","Catherine","Sophia",]

print(1, students[0])
print(2, students[1])
print(3, students[2])
print(4, students[3])
print(5, students[4])

your_pick = int(input("Select your option: 1 : Add student to the list. Select  2: Modify student name. Select 3: Remove Student:  "))
counter = 0 
if your_pick == 1:
    new_name= input("Enter your student's name to the list. ")
    students.append (new_name) 
    print("List after student has been added: ")
    for i in students:
        print(i)
elif your_pick == 2:
    print(1, students[0])
    print(2, students[1])
    print(3, students[2])
    print(4, students[3])
    print(5, students[4])

    modify_name=int(input("Enter the number of the student you would like to modify. "))
    modify_name = modify_name - 1
    new_name=input("Enter the new name:  ")

    students[modify_name] = new_name

    print("List after student has been added: ")
    for i in students:
         print (i)
elif your_pick ==3:
    print(1, students[0])
    print(2, students[1])
    print(3, students[2])
    print(4, students[3])
    print(5, students[4])

    remove_name = int(input("Enter the number of the student you would like to remove. "))
    remove_name = remove_name - 1
    students.pop(remove_name)
    print("List after student has been removed: ")
    for i in students:
         print(i)
else:
    print("Your did not enter a valid choice.")




