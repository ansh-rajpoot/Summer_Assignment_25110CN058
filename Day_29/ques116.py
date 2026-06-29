# Write a program to Create inventory
# management system.
inventory = {}

while True:

    print("\n----- Inventory Management System -----")
    print("1. Add Item")
    print("2. Display Items")

    
    print("3. Search Item")

    print("4. Update Item")
    print("5. Delete Item")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":


        item_id = input("Enter Item ID: ")

        if item_id in inventory:
            print("Item already exists.")
        else:
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))

            inventory[item_id] = [name, quantity, price]
            print("Item added successfully.")

    elif choice == "2":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("\nInventory Details")
            for item_id in inventory:
                print("Item ID  :", item_id)
                print("Name     :", inventory[item_id][0])
                print("Quantity :", inventory[item_id][1])
                print("Price    :", inventory[item_id][2])
                print()

    elif choice == "3":
        item_id = input("Enter Item ID to search: ")

        if item_id in inventory:
            print("Name     :", inventory[item_id][0])
            print("Quantity :", inventory[item_id][1])
            print("Price    :", inventory[item_id][2])
        else:
            print("Item not found.")

    elif choice =="4":
        item_id= input("Enter Item ID to update: ")

        if item_id in inventory:
            name =input("Enter New Item Name: ")
            quantity =int(input("Enter New Quantity: "))
            price = float(input("Enter New Price: "))

            inventory[item_id] = [name, quantity, price]
            print("Item updated successfully.")
        else:
            print("Item not found.")

    elif choice =="5":
        item_id= input("Enter Item ID to delete: ")

        if item_id in inventory:
            del inventory[item_id]
            print("Item deleted successfully.")
        else:
            print("Item not found.")

    elif choice =="6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")
