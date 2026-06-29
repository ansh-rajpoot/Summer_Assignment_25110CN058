# Write a program to Create ticket booking
# system.
ticket = {}

while True:
    print("\n----- Ticket Booking System -----")
    print("1. Book Ticket")
    print("2. Display Bookings")
    print("3. Search Booking")
    print("4. Update Booking")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
        ticket_id = input("Enter Ticket ID: ")

        if ticket_id in ticket:
            print("Ticket already booked.")
        else:
            name = input("Enter Passenger Name: ")
            source = input("Enter Source: ")
            destination = input("Enter Destination: ")
            fare = float(input("Enter Fare: "))

            ticket[ticket_id] = [name, source, destination, fare]
            print("Ticket booked successfully.")

    elif choice =="2":
        if len(ticket) == 0:
            print("No bookings found.")
        else:
            print("\nBooked Tickets")
            for ticket_id in ticket:
                print("Ticket ID   :", ticket_id)
                print("Name        :", ticket[ticket_id][0])
                print("Source      :", ticket[ticket_id][1])
                print("Destination :", ticket[ticket_id][2])
                print("Fare        :", ticket[ticket_id][3])
                print()

    elif choice=="3":
        ticket_id = input("Enter Ticket ID to search: ")

        if ticket_id in ticket:
            print("Name        :", ticket[ticket_id][0])
            print("Source      :", ticket[ticket_id][1])
            print("Destination :", ticket[ticket_id][2])
            print("Fare        :", ticket[ticket_id][3])
        else:

            print("Booking not found.")

    elif choice== "4":
        ticket_id =input("Enter Ticket ID to update: ")

        if ticket_id in ticket:


            name =input("Enter New Passenger Name: ")
            source = input("Enter New Source: ")
            destination = input("Enter New Destination: ")
            fare = float(input("Enter New Fare: "))

            ticket[ticket_id] = [name, source, destination, fare]
            print("Booking updated successfully.")
        else:

            print("Booking not found.")

    elif choice == "5":

        ticket_id = input("Enter Ticket ID to cancel: ")

        if ticket_id in ticket:
            del ticket[ticket_id]
            print("Ticket cancelled successfully.")
        else:

            print("Booking not found.")

    elif choice == "6":
        print("Program Ended.")
        break



    else:
        print("Invalid choice.")