# Write a program to Create bank account
# system.
bank = {}

while True:
    print("\n----- Bank Account Management System -----")
    print("1. Create Account")
    print("2. Display Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Delete Account")
    print("7. Exit")

    choice =input("Enter your choice: ")

    if choice =="1":
        acc_no = input("Enter Account Number: ")

        if acc_no in bank:
            print("Account already exists.")
        else:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            bank[acc_no] = [name, balance]
            print("Account created successfully.")

    elif choice== "2":
        if len(bank) == 0:
            print("No accounts found.")
        else:
            print("\nBank Accounts")
            for acc_no in bank:
                print("Account Number :", acc_no)
                print("Name           :", bank[acc_no][0])
                print("Balance        :", bank[acc_no][1])
                print()

    elif choice =="3":
        acc_no = input("Enter Account Number to search: ")

        if acc_no in bank:
            print("Name    :", bank[acc_no][0])
            print("Balance :", bank[acc_no][1])
        else:
            print("Account not found.")

    elif choice== "4":
        acc_no = input("Enter Account Number: ")

        if acc_no in bank:
            amount = float(input("Enter Deposit Amount: "))
            bank[acc_no][1] += amount
            print("Amount deposited successfully.")
            print("New Balance:", bank[acc_no][1])
        else:
            print("Account not found.")

    elif choice =="5":
        acc_no = input("Enter Account Number: ")

        if acc_no in bank:
            amount = float(input("Enter Withdraw Amount: "))

            if amount <= bank[acc_no][1]:
                bank[acc_no][1] -= amount
                print("Amount withdrawn successfully.")
                print("Remaining Balance:", bank[acc_no][1])
            else:
                print("Insufficient Balance.")
        else:
            print("Account not found.")
    elif choice == "6":
        acc_no = input("Enter Account Number to delete: ")

        if acc_no in bank:
            del bank[acc_no]
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    elif choice == "7":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.")