# Write a program to Create menu-driven string operations system

string = input("Enter a string: ")

while True:

    print("\n----- String Operations -----")
    print("1. Display String")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Find Length")
    print("5. Reverse String")
    print("6. Search Character")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("String =", string)

    elif choice=="2":
        print("Uppercase =", string.upper())

    elif choice == "3":
        print("Lowercase =", string.lower())

    elif choice=="4":


        print("Length =", len(string))

    elif choice =="5":
        print("Reversed =", string[::-1])

    elif choice== "6":
        ch = input("Enter character to search: ")

        if ch in string:
            print("Character found at index", string.index(ch))
        else:

            print("Character not found.")

    elif choice=="7":


        print("Program Ended.")
        break

    else:

        print("Invalid choice.")