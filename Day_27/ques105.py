# Write a program to Create student record
# management system
# Student Record Management System

students={}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Age": age,
        "Marks": marks
    }
    print("Student added successfully.\n")
def display_students():
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Records")
    print("-" * 45)
    print("Roll\tName\t\tAge\tMarks")
    print("-" * 45)

    for roll, details in students.items():
        print(f"{roll}\t{details['Name']}\t\t{details['Age']}\t{details['Marks']}")
    print()


def search_student():
    roll =input("Enter Roll Number to search: ")

    if roll in students:
        s = students[roll]
        print("\nStudent Found")
        print("Roll :", roll)
        print("Name :", s["Name"])
        print("Age  :", s["Age"])
        print("Marks:", s["Marks"])
    else:
        print("Student not found.")
    print()


def update_student():
    roll= input("Enter Roll Number to update: ")

    if roll in students:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        marks = float(input("Enter New Marks: "))

        students[roll]["Name"] = name
        students[roll]["Age"] = age
        students[roll]["Marks"] = marks

        print("Record updated successfully.\n")
    else:
        print("Student not found.\n")


def delete_student():
    roll =input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Student record deleted.\n")
    else:
        print("Student not found.\n")


while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice== "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice =="4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Please try again.\n")