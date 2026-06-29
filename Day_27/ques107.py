# Write a program to Create salary management
# system.

salary = {}

while True:
    print("\n----- Salary Management System -----")
    print("1. Add Employee Salary")
    print("2. Display Salary Records")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        if emp_id in salary:
            print("Employee already exists.")
        else:
            name = input("Enter Employee Name: ")
            basic = float(input("Enter Basic Salary: "))
            bonus = float(input("Enter Bonus: "))

            total = basic + bonus

            salary[emp_id] = [name, basic, bonus, total]

            
            print("Salary record added successfully.")

    elif choice == "2":
        if len(salary) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records")
            for emp_id in salary:
                print("Employee ID :", emp_id)
                print("Name         :", salary[emp_id][0])
                print("Basic Salary :", salary[emp_id][1])
                print("Bonus        :", salary[emp_id][2])
                print("Total Salary :", salary[emp_id][3])
                print()

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in salary:
            print("Name         :", salary[emp_id][0])
            print("Basic Salary :", salary[emp_id][1])
            print("Bonus        :", salary[emp_id][2])
            print("Total Salary :", salary[emp_id][3])
        else:

            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ")



        if emp_id in salary:
            name = input("Enter New Name: ")
            basic = float(input("Enter New Basic Salary: "))
            bonus = float(input("Enter New Bonus: "))

            total = basic + bonus

            salary[emp_id] = [name, basic, bonus, total]

            print("Salary updated successfully.")
        else:
            print("Employee not found.")

    elif choice== "5":
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in salary:
            del salary[emp_id]
            print("Record deleted successfully.")
        else:
            print("Employee not found.")

    elif choice =="6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")