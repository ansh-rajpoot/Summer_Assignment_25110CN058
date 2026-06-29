# Write a program to Create menu-driven
# calculator.
while True:

    print("\n----- Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        num1 = float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        result=num1 + num2
        print("Result =", result)

    elif choice == "2":
        num1=float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1-num2
        print("Result =",result)

    elif choice=="3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result=num1 * num2
        print("Result =", result)

    elif choice == "4":
        
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))

        if num2 !=0:
            result = num1 / num2
            print("Result =", result)
        else:
            print("Cannot divide by zero.")

    elif choice=="5":

        print("Program Ended.")
        break

    else:
        print("Invalid choice.")