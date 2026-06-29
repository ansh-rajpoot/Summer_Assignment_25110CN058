# Write a program to Create student record system using arrays and strings
students = []

while True:
    print("\n----- Student Record System -----")
    print("1. Add Student")

    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")

    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice== "1":


        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")

        course = input("Enter Course: ")

        students.append([roll, name, course])
        print("Student added successfully.")

    elif choice =="2":
        if len(students)==0:
            print("No records found.")
        else:
            for i in students:
                print("Roll Number :", i[0])
                print("Name        :", i[1])

                print("Course      :", i[2])
                print()

    elif choice =="3":
        roll = input("Enter Roll Number to search: ")

        found = False

        for i in students:
            if i[0] == roll:
                print("Roll Number :", i[0])
                print("Name        :", i[1])
                print("Course      :", i[2])
                found = True
                break

        if found ==False:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        found =False

        for i in students:
            if i[0] == roll:
                i[1] = input("Enter New Name: ")
                i[2] = input("Enter New Course: ")
                print("Record updated.")
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":
        roll = input("Enter Roll Number to delete: ")

        found = False

        for i in students:
            if i[0] ==roll:
                students.remove(i)
                print("Record deleted.")
                found =True
                break
        if found == False:
            print("Student not found.")

    elif choice == "6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")