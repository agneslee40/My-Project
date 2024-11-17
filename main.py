import os
import datetime
from datetime import timedelta
import random

## Tools
# Error message format
def error_msg(msg):
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("| ERROR: Invalid Input! " + msg + " |")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Please try again.\n")

# validation of select menu option
def validate_input(option, maxOption):
    # Check if input is a number
    if option.isdigit():
        # Check if input is within range
        if int(option) in range(1, maxOption + 1):
            return True
        else:
            error_msg("Please enter a number between 1 and " + str(maxOption) + ".")
            return False
    else:
        print(">>> Invalid input! Please enter a number between 1 and " + str(maxOption) + ".")
        return False

## Initialize Program
# Global variables
reserve_list = []
menu_list = []

#read reservations from textfiles line by line then add into list
def read_reservation():
    reservation_file = 'reservation.txt'
    with open(reservation_file,'r') as f:
        for line in f:
            if line != "\n":
                reserve_list.append(line.strip().split("|"))
    f.close()
    
#read menu items from textfiles line by line then add into list
def read_menuItems():
    menu_file = 'menuItems.txt'
    with open(menu_file,'r') as f:
        for line in f:
            if line != "\n":
                menu_list.append(line.strip())
    f.close()

## Terminate Program
# write reservations from list into textfiles line by line
def write_reservation():
    reservation_file = 'reservation.txt'
    with open(reservation_file,'w') as f:
        for line in reserve_list:
            f.write("|".join(line) + "\n")
    f.close()

## Generate meal recommendation
def generate_meal_rec():
    os.system("cls")

    print(">>> GENERATE MEAL RECOMMENDATION MENU")

    # Display options in the meal recommendation menu
    while True:
        print()
        print("[1] View full menu\n" +
                "[2] Generate recommended dish\n")

        option = input("--- Selection (enter 1 or 2 only):\n>>> ")
        if(validate_input(option, 2)):
        # Option to view full menu
            if option == "1":
                print("\n>>> CHARMING THYME TRATTORIA KUALA LUMPUR MENU")
                count = 1
                for x in menu_list:
                    print(f"{count}. {x}")
                    count += 1
                print()
                break
            # Option to generate recommended dish
            elif option == "2":
                mealrandom = random.choice(menu_list)
                print(f"\n>>> Recommended dish: {mealrandom}\n")
                break

    while True:
        # Ask if the user wants to generate another recommended dish
        generateAgain = input("--- Would you like to generate recommended dish? (Y for yes,N for no):\n>>> ")
        if generateAgain.upper() == "N":
            break
        elif generateAgain.upper() == "Y":
            print()
            mealrandom = random.choice(menu_list)
            print(f">>> Recommended dish: {mealrandom}\n")
        else:
            error_msg("Please enter Y or N only")

    return 1

## Display all booking records
def display_slot(slot):
    if(slot == "Slot 1"):
        displayText = slot + " (12:00pm - 02:00pm)"
    elif(slot == "Slot 2"):
        displayText = slot + " (02:00pm - 04:00pm)"
    elif(slot == "Slot 3"):
        displayText = slot + " (06:00pm - 08:00pm)"
    elif(slot == "Slot 4"):
        displayText = slot + " (08:00pm - 10:00pm)"
    return displayText

def display_all_booking():
    # Print all booking records header
    print("=" * 135)
    print("{:^5}{:<13}{:<28}{:<25}{:<30}{:^20}{:^14}".format("NO.", "DATE", "SLOTS", "NAME", "EMAIL",
                                                                         "PHONE NUMBER", "NO. OF GUESTS"))

    # Print all booking records in a table
    for i in range(len(reserve_list)):
        # convert slot number to slot + time format
        slot = display_slot(reserve_list[i][1])
        print("{:^5}{:<13}{:<28}{:<25}{:<30}{:^20}{:^14}".format(i+1, reserve_list[i][0], slot,
                                                                         reserve_list[i][2], reserve_list[i][3],
                                                                         reserve_list[i][4], reserve_list[i][5]))
    
    print("=" * 135)
    print("\nPress enter key to exit...")
    input()
    return 1

# Search for booking records under a person's name
def search_reservation():
    os.system("cls")
    print(">>> SEARCH BOOKING\n")
    name = input("--- Booking under the name of: ")
    
    print("=" * 135)
    print("{:^5}{:<13}{:<28}{:<25}{:<30}{:^20}{:^14}".format("NO.", "DATE", "SLOTS", "NAME", "EMAIL",
                                                                            "PHONE NUMBER", "NO. OF GUESTS"))

    count = 0
    for i in range(len(reserve_list)):
        if (name.upper() == reserve_list[i][2]):
            slot = display_slot(reserve_list[i][1])
            print("{:^5}{:<13}{:<28}{:<25}{:<30}{:^20}{:^14}".format(i+1, reserve_list[i][0], slot,
                                                                            reserve_list[i][2], reserve_list[i][3],
                                                                            reserve_list[i][4], reserve_list[i][5]))
            count += 1

    print("=" * 135)
    if (count == 0):
        print(f">>> NO BOOKINGS FOUND UNDER {name.upper()}")
    else:
        print(f">>> TOTAL NO. OF BOOKINGS FOUND UNDER {name.upper()}: {count}")

    while True:
        confirm = input("\n--- Continue searching? (Y/N): \n>>> ")
        confirm = confirm.strip().upper()
        if (confirm == "Y" or confirm == "YES"):
            search_reservation()
        elif (confirm == "N" or confirm == "NO"):
            return 1
        else:
            print("Invalid input. Please try again.")
           
def display_reservation():
    while True:
        os.system("cls")
        print(">>> RESERVATION RECORD MENU\n")
        print("[1] Display all booking records\n" +
                "[2] Search for booking records under a person's name\n" +
                "[3] Back to main menu\n" )
        
        option = input("--- Enter the corresponding number for your desired options: ")
        
        while not validate_input(option, 3):
            option = input("--- Enter the corresponding number for your desired options: ")

        if(option == "1"):
            display_all_booking() 
        elif(option == "2"):
            search_reservation()
        elif(option == "3"):
            return 1

## Update/edit reservation
def update_reservation():
    while True:
        os.system("cls")
        print(">>> UPDATE RESERVATION MENU\n")
        print("Please enter the following details of the booking you would like to change: ")
        while True:
            date = input("--- Enter the date of reservation (YYYY-MM-DD) that you want to check \n>>> ")
            if (check_datetime_format(date)):
                break

        name, email, phone, pax, slot = user_input_reservation("modify reservation", "")

        # Store inputs from user into a list called checklist
        checklist = [date, "Slot "+slot, name.upper(), email.lower(), phone, pax]

        # Check if information enetered by user matches with records in reservation data
        if checklist in reserve_list:
            print(">>> Record Found, please enter your new information for the booking:")
            confirm_reservation, form_data = verify_reservation_session()
            if (confirm_reservation):
                for i in range(len(reserve_list)):
                    if checklist == reserve_list[i]:
                        reserve_list[i] = form_data
                        break
                print(">>> Your booking has been updated.")
            else:
                print("\n>>> CANCELLED: You have cancelled your modification.")
        else:
            print()
            print(">>> Sorry, no record found.")
            print()

        print("\nWould you like to modify another booking or return to MAIN MENU?")
        print("[1] Modify another booking")
        print("[2] Return to MAIN MENU\n")
        option = input("--- Enter the corresponding number for your desired options: ")
        while not validate_input(option, 2):
            option = input("--- Enter the corresponding number for your desired options: ")
        
        if(option == "1"):
            continue
        elif(option == "2"):
            return 1

## Cancel reservation
def cancel_reservation():
    while True:
        os.system("cls")
        print(">>> CANCEL MENU")
        print()
        # Get user's input and use it to trace the record to be deleted
        print("Please enter the following details to cancel your reservation:")
        while True:
            date = input("--- Enter the date of reservation (YYYY-MM-DD) that you want to check \n>>> ")
            if (check_datetime_format(date)):
                break

        name, email, phone, pax, slot = user_input_reservation("modify reservation", "")

        # Store inputs from user into a list called checklist
        checklist = [date, "Slot "+slot, name.upper(), email.lower(), phone, pax]

        # Check if information enetered by user matches with records in reservation data
        if checklist in reserve_list:
            for i in range(len(reserve_list)):
                if checklist == reserve_list[i]:
                    reserve_list.pop(i)
                    break
            print(">>> Record Found, your booking has been cancelled.")
        else:
            print()
            print(">>> Sorry, no record found.")
            print()

        print("\nWould you like to cancel another booking or return to MAIN MENU?")
        print("[1] Cancel another booking")
        print("[2] Return to MAIN MENU\n")
        option = input("--- Enter the corresponding number for your desired options: ")
        while not validate_input(option, 2):
            option = input("--- Enter the corresponding number for your desired options: ")
        
        if(option == "1"):
            continue
        elif(option == "2"):
            return 1

## Add reservation
def check_datetime_format(data):
    validate = False
    # Check if date is in correct format (YYYY-MM-DD)
    try:
        # strptime throws an exception if the input doesn't match the pattern
        validate = bool(datetime.datetime.strptime(data, '%Y-%m-%d'))
    except ValueError:
        print("Incorrect date format! Please try again")
        validate = False

    return validate

# validation of name, email, phone number, pax, date, slot
def validate_reservation_input(type, data, date_slots = []):
    validate = False
    try:
        if type == "name":
            validate = len(data) > 0 and not data.isdigit()

        elif type == "email":
            for i in range(len(data)):
                if (data[i] == "@"):
                    if (data[i+1] == "."):
                        validate = False
                        break
                    else:
                        validate = True
                        break
        
        elif type == "phone":
            if (data.isdigit() and len(data) == 10):
                validate = True
        
        elif type == "pax":
            data = int(data)
            validate = data > 0 and data <= 4

        elif type == "date":
            # Check if date is today's date
            if (data == datetime.date.today().strftime("%Y-%m-%d")):
                print("Sorry, the reservation date cannot be the same as the current date")
                validate = False
            
            # Check if date is at least 5 days in advance
            min_reservation_date = (datetime.date.today() + timedelta (days=5)).strftime("%Y-%m-%d")

            if (data >= min_reservation_date):
                # Check if date is in correct format
                if(check_datetime_format(data)):
                    validate = True
            else:
                print("Sorry, the reservation must be booked at least 5 days advance! Please try again")
                validate = False

        elif type == "slot add reservation":
            # Check if slot is within range (1-4)
            data = int(data)
            if (data > 0 and data <= 4):
                if (date_slots[data-1] == 0):
                    print("Sorry, the slot you have selected is full. Please try again.")
                    validate = False
                else:
                    validate = True

        elif type == "slot modify reservation":
            data = int(data)
            # Check if slot is within range (1-4)
            validate = data > 0 and data <= 4

    except ValueError:
        validate = False
    
    return validate

def write_reservation_to_file(filename, data):
    with open(filename, "a+") as file:
        file.write(data + "\n")
    file.close()

def check_slots_number(date):
    current_reservation_slots = [8, 8, 8, 8]

    for i in reserve_list:
        if i[0] == date and i[1] == "Slot 1":
            current_reservation_slots[0] -= 1
        elif i[0] == date and i[1] == "Slot 2":
            current_reservation_slots[1] -= 1
        elif i[0] == date and i[1] == "Slot 3":
            current_reservation_slots[2] -= 1
        elif i[0] == date and i[1] == "Slot 4":
            current_reservation_slots[3] -= 1
    
    return current_reservation_slots

def verify_reservation_session():
    print("\nToday date is: " + datetime.date.today().strftime("%Y-%m-%d"))
    print("The date you can make reservation was after: " + (datetime.date.today() + timedelta (days=5)).strftime("%Y-%m-%d") + "\n")

    while True:
        date = input("--- Enter the date of reservation (YYYY-MM-DD) that you want to check \n>>> ")
        if (validate_reservation_input("date", date)):
            break
    
    date_slots = check_slots_number(date)
    display_session_slots(date, date_slots)

    confirm_reservation = False

    while True:
        confirm = input("\n--- Would you like to make a reservation? (Y for yes, N for No): \n>>> ")
        confirm = confirm.strip().upper()
        if (confirm == "Y" or confirm == "YES"):
            name, email, phone, pax, slot = user_input_reservation("add reservation",date_slots)
            form_data = [date, "Slot " + str(slot), name.upper(), email, phone, str(pax)]
            confirm_reservation = True
            break
        elif (confirm == "N" or confirm == "NO"):
            return False, ""
        else:
            print("Invalid input. Please try again.")

    return confirm_reservation, form_data

def display_session_slots(date, date_slots):
    print("\nThe slots for " + date + " are: ")
    print(str(date_slots[0]) + " available slots for Slot 1: 12:00pm - 02:00pm")
    print(str(date_slots[1]) + " available slots for Slot 2: 02:00pm - 04:00pm")
    print(str(date_slots[2]) + " available slots for Slot 3: 06:00pm - 08:00pm")
    print(str(date_slots[3]) + " available slots for Slot 4: 08:00pm - 10:00pm")

    if (date_slots[0] == 0 and date_slots[1] == 0 and date_slots[2] == 0 and date_slots[3] == 0):
        print("\nSorry, there are no available slots for " + date + ". Please try another date.\n")
        verify_reservation_session()

def user_input_reservation(function, date_slots):
    if(function == "add reservation"):
        while True:
            slot = input("--- Enter the number of slot: \n>>> ")
            if validate_reservation_input("slot add reservation", slot, date_slots):
                break
            else:
                print("Invalid number of slot. Please try again.")
    elif(function == "modify reservation"):
        while True:
            slot = input("--- Enter the number of slot: \n>>> ")
            if validate_reservation_input("slot modify reservation", slot):
                break
            else:
                print("Invalid number of slot. Please try again.")
    
    while True:
        name = input("--- Enter your name: \n>>> ")
        if validate_reservation_input("name", name):
            break
        else:
            print("Invalid name. Please try again.")
    
    while True:
        email = input("--- Enter your email: \n>>> ")
        if validate_reservation_input("email", email):
            break
        else:
            print("Invalid email. Please try again.")
    
    while True:
        phone = input("--- Enter your phone number (10 digits only): \n>>> ")
        if validate_reservation_input("phone", phone):
            break
        else:
            print("Invalid phone number. Please try again.")
    
    while True:
        pax = input("--- Enter number of people (Max 4 people): \n>>> ")
        if validate_reservation_input("pax", pax):
            break
        else:
            print("Invalid number of people. Please try again.")

    return name.upper(), email, phone, pax, slot

def add_reservation():
    while True:
        os.system("cls")
        print(">>> ADD RESERVATION MENU")
        confirm_reservation, form_data = verify_reservation_session()
        if (confirm_reservation):
            reserve_list.append(form_data)
            print("\n>>> SUCCESSFULLY BOOKED: You have successfully made a reservation, thank you for choosing us!")
        else:
            print("\n>>> CANCELLED: You have cancelled your reservation.")

        print("\n>>> Would you like to: ")
        print("[1] Return to MAIN MENU\n" +
            "[2] Add another reservation\n")
        
        option = input("--- Selection [1 or 2 only]:\n>>> ")

        while not validate_input(option, 2):
            option = input("--- Selection [1 or 2 only]:\n>>> ")

        if(option == "1"):
            return 1
        elif(option == "2"):
            continue


## Initialize Program
read_reservation()
read_menuItems()

## Main
while True:
    os.system("cls")
    print(">>> Charming Thyme Trattoria Kuala Lumpur Booking Site\n")
    print(">>> Welcome to the MAIN MENU of our booking site, please select from the following options:")

    # Display available options to user in MAIN MENU
    print("\n>>> MAIN MENU")
    print("[1] Add Reservation\n" +
          "[2] Cancel Reservation\n" +
          "[3] Update/Edit Reservation\n" +
          "[4] Display Reservation Record\n" +
          "[5] Generate Meal Recommendation\n" +
          "[6] Exit\n")
    
    # Prompt user to select from available options
    option = input("--- Enter the corresponding number (1, 2, 3, 4, 5 or 6) for your desired options: ")

    # Validate user input
    while not validate_input(option, 6):
        option = input("--- Enter the corresponding number (1, 2, 3, 4, 5 or 6) for your desired options: ")
    
    # Clear screen
    os.system("cls")

    if(option == "1"):
        add_reservation()
    elif(option == "2"):
        cancel_reservation()
    elif(option == "3"):
        update_reservation()
    elif(option == "4"):
        display_reservation()
    elif(option == "5"):
        generate_meal_rec()
    elif(option == "6"):
        write_reservation()
        print(">>> Thank you for using our booking site. Have a nice day!")
        exit()
