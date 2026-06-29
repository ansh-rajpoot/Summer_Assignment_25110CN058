# Write a program to Create ATM simulation.
def atm_simulation():
    balance = 5000
    pin = 1234
    is_authenticated =False
    
    user_pin = int(input("Enter your 4-digit ATM PIN: "))
    
    if user_pin == pin:
        is_authenticated = True
    else:
        print("\nIncorrect PIN! Access Denied.")
        
    while is_authenticated:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = int(input("\nEnter your choice (1-4): "))
        
        if choice ==1:
            print(f"\nYour current balance is:- Rs. {balance}")
        elif choice== 2:
            amount =int(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Rs. {amount} deposited successfully!")
                print(f"New balance is:- Rs. {balance}")
            else:
                print("Invalid deposit amount!")
        elif choice ==3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Invalid withdrawal amount!")
            else:
                balance -= amount
                print(f"Rs. {amount} withdrawn successfully!")
                print(f"Remaining balance is:- Rs. {balance}")
        elif choice== 4:
            print("\nThank you for using our ATM.")
            is_authenticated = False
        else:
            print("Invalid choice! Please select a valid option.")

atm_simulation()
