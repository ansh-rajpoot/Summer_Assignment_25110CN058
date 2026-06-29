# Write a program to Create marksheet
# generation system.

marksheet={}

while True:
    print("\n----- Marksheet Generation System -----")
    print("1. Add Student")
    print("2. Display Marksheets")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":
        roll = input("Enter Roll Number: ")

        if roll in marksheet:
            print("Student already exists.")
        else:
            name = input("Enter Student Name: ")
            m1 = int(input("Enter Marks in Subject 1: "))
            m2 = int(input("Enter Marks in Subject 2: "))
            m3 = int(input("Enter Marks in Subject 3: "))

            total = m1 + m2 + m3
            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >=75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >=40:
                grade = "C"
            else:
                grade = "Fail"

            marksheet[roll] = [name, m1, m2, m3, total, percentage, grade]

            print("Marksheet generated successfully.")
    elif choice == "2":
        if len(marksheet) == 0:
            print("No records found.")
        else:
            for roll in marksheet:
                print("\nRoll Number :", roll)
                print("Name        :", marksheet[roll][0])
                print("Subject 1   :", marksheet[roll][1])
                print("Subject 2   :", marksheet[roll][2])
                print("Subject 3   :", marksheet[roll][3])
                print("Total       :", marksheet[roll][4])
                print("Percentage  :", round(marksheet[roll][5], 2))
                print("Grade       :", marksheet[roll][6])

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        if roll in marksheet:
            print("Name        :", marksheet[roll][0])
            print("Total       :", marksheet[roll][4])
            print("Percentage  :", round(marksheet[roll][5], 2))
            print("Grade       :", marksheet[roll][6])
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        if roll in marksheet:
            name = input("Enter New Name: ")
            m1 = int(input("Enter New Subject 1 Marks: "))
            m2 = int(input("Enter New Subject 2 Marks: "))
            m3 = int(input("Enter New Subject 3 Marks: "))

            total = m1 + m2 + m3
            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 75:
                grade = "A"
            elif percentage >=60:
                grade = "B"
            elif percentage >= 40:
                grade = "C"
            else:
                grade = "Fail"

            marksheet[roll] =[name, m1, m2, m3, total, percentage, grade]

            print("Record updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        roll = input("Enter Roll Number to delete: ")

        if roll in marksheet:
            del marksheet[roll]
            print("Record deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")