# Write a program to Create mini library system

# Mini Library System

books=[]

while True:

    print("\n----- Mini Library System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice== "1":
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book added successfully.")

    elif choice =="2":


        if len(books)==0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i in books:
                print(i)

    elif choice == "3":
        book = input("Enter Book Name to search: ")
        if book in books:
            print("Book is available.")
        else:
            print("Book not found.")

    elif choice== "4":
        book = input("Enter Book Name to issue: ")

        if book in books:
            books.remove(book)
            print("Book issued successfully.")
        else:

            print("Book not available.")

    elif choice == "5":
        book = input("Enter Book Name to return: ")
        books.append(book)

        print("Book returned successfully.")
    elif choice == "6":

        print("Program Ended.")
        break


    else:
        print("Invalid choice.")