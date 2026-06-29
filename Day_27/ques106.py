# Write a program to Create employee
# management system.
employee = {}

while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employee:
            print("Employee already exists.")
        else:
            name = input("Enter Employee Name: ")
            age = input("Enter Employee Age: ")
            dept = input("Enter Department: ")
            salary = input("Enter Salary: ")

            employee[emp_id] = [name, age, dept, salary]
            print("Employee added successfully.")

    elif choice == "2":
        if len(employee) ==0:
            print("No employee records found.")
        else:
            print("\nEmployee Details")
            for emp_id in employee:
                print("Employee ID :", emp_id)
                print("Name        :", employee[emp_id][0])
                print("Age         :", employee[emp_id][1])
                print("Department  :", employee[emp_id][2])
                print("Salary      :", employee[emp_id][3])
                print()

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in employee:
            print("Employee Found")
            print("Name       :", employee[emp_id][0])
            print("Age        :", employee[emp_id][1])
            print("Department :", employee[emp_id][2])
            print("Salary     :", employee[emp_id][3])
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ")

        if emp_id in employee:
            employee[emp_id][0] =input("Enter New Name: ")
            employee[emp_id][1]= input("Enter New Age: ")
            employee[emp_id][2] =input("Enter New Department: ")
            employee[emp_id][3] = input("Enter New Salary: ")
            print("Employee record updated.")
        else:
            print("Employee not found.")

    elif choice == "5":
        emp_id = input("Enter Employee ID to delete: ")

        if emp_id in employee:
            del employee[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")
    elif choice == "6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")