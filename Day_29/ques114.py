#Write a program to Create menu-driven array operations system.

arr = []

while True:

    print("\n----- Array Operations -----")
    print("1. Insert Element")
    print("2. Delete Element")
    print("3. Search Element")
    print("4. Update Element")
    print("5. Display Array")
    print("6. Sort Array")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("Enter element: "))
        arr.append(num)
        print("Element inserted.")

    elif choice=="2":
        num = int(input("Enter element to delete: "))

        if num in arr:
            arr.remove(num)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == "3":
        num=int(input("Enter element to search: "))

        if num in arr:
            print("Element found at index", arr.index(num))
        else:
            print("Element not found.")

    elif choice=="4":
        old = int(input("Enter element to update: "))

        if old in arr:
            new = int(input("Enter new element: "))
            index = arr.index(old)
            arr[index] = new
            print("Element updated.")
        else:
            print("Element not found.")

    elif choice == "5":
        if len(arr)==0:
            print("Array is empty.")
        else:
            print("Array =", arr)
    elif choice=="6":
        arr.sort()
        print("Array sorted.")
        print("Array =", arr)

    elif choice=="7":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")