# Write a program to Create library
# management system.

library = {}

while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice =input("Enter your choice: ")

    if choice=="1":
        book_id=input("Enter Book ID: ")

        if book_id in library:
            print("Book already exists.")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            quantity = int(input("Enter Quantity: "))

            library[book_id] = [title, author, quantity]
            print("Book added successfully.")

    elif choice == "2":
        if len(library) ==0:
            print("No books available.")
        else:
            print("\nLibrary Books")
            for book_id in library:
                print("Book ID  :", book_id)
                print("Title    :", library[book_id][0])
                print("Author   :", library[book_id][1])
                print("Quantity :", library[book_id][2])
                print()

    elif choice=="3":
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            print("Title    :", library[book_id][0])
            print("Author   :", library[book_id][1])
            print("Quantity :", library[book_id][2])
        else:
            print("Book not found.")

    elif choice== "4":
        book_id = input("Enter Book ID to update: ")

        if book_id in library:
            title = input("Enter New Title: ")
            author = input("Enter New Author: ")
            quantity = int(input("Enter New Quantity: "))

            library[book_id] = [title, author, quantity]
            print("Book updated successfully.")
        else:
            print("Book not found.")

    elif choice =="5":
        book_id = input("Enter Book ID to delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    elif choice =="6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")