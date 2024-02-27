def process_date_data():
    try:
        day = int(input("Enter the day: "))
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        syear = year % 4
        if 1 <= day <= 31 and 1 <= month <= 12:
            print(f"The date {day}/{month}/{year} is valid.")
        else:
            print("Invalid date.")
    except ValueError:
        print("Invalid input. Please enter valid value (dd mm yyyy).")

def process_character_data():
    try:
        schar = input("Enter first character: ")
        echar = input("Enter second character: ")

        for char in range(ord(echar)+1, ord(schar)):
            print(f"{chr(char)}: {char}, {hex(char)}h")
    except TypeError:
        print("Invalid input. Please enter valid characters.")

while True:
    print("\nMenu:")
    print("1- Process Date Data")
    print("2- Process Character Data")
    print("3- Quit")

    choose = input("Choose an operation: ")

    if choose == '1':
        process_date_data()
    elif choose == '2':
        process_character_data()
    elif choose == '3':
        print("Exiting!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

