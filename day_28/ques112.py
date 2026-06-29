# Write a program to Create contact
# management system.

contact ={}


while True:


    print("\n----- Contact Management System -----")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":

        phone = input("Enter Phone Number: ")
        if phone in contact:
            print("Contact already exists.")
        else:
            
            name = input("Enter Name: ")
            email = input("Enter Email: ")

            contact[phone] = [name, email]
            print("Contact added successfully.")
    elif choice== "2":
        if len(contact) == 0:
            print("No contacts found.")
        else:
            print("\nContact List")
            for phone in contact:
                print("Phone :", phone)
                print("Name  :", contact[phone][0])
                print("Email :", contact[phone][1])
                print()
    elif choice == "3":
        phone = input("Enter Phone Number to search: ")
        if phone in contact:
            print("Name  :", contact[phone][0])
            print("Email :", contact[phone][1])
        else:
            print("Contact not found.")

    elif choice== "4":
        phone = input("Enter Phone Number to update: ")
        if phone in contact:
            name = input("Enter New Name: ")
            email = input("Enter New Email: ")

            contact[phone] = [name, email]
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice =="5":
        phone=input("Enter Phone Number to delete: ")

        if phone in contact:
            del contact[phone]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")