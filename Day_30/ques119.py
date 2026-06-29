# Write a program to Create mini employee management system.

# Mini Employee Management System

employees = []

while True:

    print("\n----- Mini Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Exit")

    choice =input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")

        employees.append([emp_id, name, department])
        print("Employee added successfully.")

    elif choice== "2":
        if len(employees)==0:
            print("No employee records found.")
        else:
            print("\nEmployee Details")
            for i in employees:
                print("ID         :", i[0])
                print("Name       :", i[1])
                print("Department :", i[2])
                print()

    elif choice == "3":
        emp_id= input("Enter Employee ID to search: ")

        found=False

        for i in employees:
            if i[0] == emp_id:
                print("ID         :", i[0])
                print("Name       :", i[1])
                print("Department :", i[2])
                found = True
                break

        if found ==False:
            print("Employee not found.")

    elif choice =="4":
        emp_id= input("Enter Employee ID to remove: ")

        found = False
        for i in employees:
            if i[0] ==emp_id:
                employees.remove(i)
                print("Employee removed successfully.")
                found = True
                break

        if found== False:
            print("Employee not found.")

    elif choice== "5":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")