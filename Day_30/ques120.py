# Write a program to Develop complete mini project using arrays, strings and functions.
books=[]

def add_book():
    name= input("Enter Book Name: ")
    books.append(name)
    print("Book added successfully.")

def display_books():
    if len(books)==0:
        print("Library is empty.")
    else:
        print("\nAvailable Books:")
        for i in books:
            print(i)

def search_book():
    name =input("Enter Book Name to search: ")

    if name in books:
        print("Book is available.")
    else:
        print("Book not found.")

def issue_book():
    name= input("Enter Book Name to issue: ")

    if name in books:
        books.remove(name)
        print("Book issued successfully.")
    else:
        print("Book not available.")

def return_book():
    name =input("Enter Book Name to return: ")
    books.append(name)
    print("Book returned successfully.")

while True:

    print("\n----- Mini Library System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice =input("Enter your choice: ")

    if choice=="1":
        add_book()

    elif choice=="2":
        display_books()

    elif choice=="3":
        search_book()

    elif choice=="4":
        issue_book()

    elif choice=="5":
        return_book()

    elif choice=="6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")


                  









                                 ###  ------------------ASSIGNMENT COMPLETED-------------------------  ###