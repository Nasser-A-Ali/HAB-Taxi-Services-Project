# DESCRIPTION: This is a smaller program that will be brought into a larger program as a part of the Final Sprint for Semester 1. This program will start with a user input of the drivers number (or employee number) and return a report of their insurance policy informaton.
# AUTHOR: Brian Janes
# DATE: April 1st, 2024

import FormatValues as FV

# ANSII escape codes to colour text in the terminal.
# Define ANSII escape codes for colors
# I have really enjoyed using these colours in the terminal, and I think they make the program look a lot better.
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"

def driver_num_input():
    """
    This function will get the driver number from the user. It will only accept a 4 digit number right now.
    """
    while True:
        try:
            print()
            driver_num = int(
                input("Please enter the driver's number (####): "))
            print()
            if not driver_num in range(1000, 9999):
                print(
                    f"{RED}Data Entry Error - Driver number must be a 4 digit number. Please try again.{RESET}"
                )
                print()
                continue
            break
        except ValueError:
            print()
            print(
                f"{RED}Data Entry Error - Driver number must be a 4 digit number. Please try again.{RESET}"
            )
            print()
    FV.clear_terminal()
    return driver_num


def format_employee_data(employee_data):
    """
    This function takes in the employee object from employee_data and formats it for display later in the program. It uses the keys created above so as long as those stay the same it should work.
    Returns a tuple of formatted data, to be deconstructed later.
    """
    # Formatting dollar values, and names, and other displays that felt appropriate to format.
    formatted_insurance_name = employee_data["insurance_company"].title()
    formatted_name = f"{employee_data["first_name"].title()} {
        employee_data["last_name"].title()}"
    formatted_license_num = employee_data["license_num"].upper()
    formatted_driver_num = employee_data["driver_num"]
    owns_car_display = "Yes" if employee_data["own_car"] == "Y" else "No"
    formatted_insurance_num = employee_data["insurance_num"].upper()

    # Returning a tuple of formatted data to be deconstructed later.
    return (
        formatted_insurance_name,
        formatted_name,
        formatted_license_num,
        formatted_driver_num,
        owns_car_display,
        formatted_insurance_num,
    )


def find_employee(employee_data, driver_number):
    """
    This function will loop through the employee data to find the employee with the driver number entered by the user.
    It will return "None" if the driver number is not found, and this error will be handled later in the program.
    """
    for employee in employee_data:
        if employee["driver_num"] == str(driver_number):
            return employee
    return None


def insurance_report(employee_data):
    """
    This function will display the insurance report for the employee based on the driver number entered by the user.
    """

    FV.clear_terminal()

    while True:
        driver_number = driver_num_input()
        employee = find_employee(employee_data, driver_number)

        # This is just a function I made in my other file to give the user the feeling that the request is being processed.
        FV.processing_blinker()
        FV.clear_terminal()

        if employee is not None:
            # Deconstructing the info from format_employee_data to be printed.
            (
                formatted_insurance_name,
                formatted_name,
                formatted_license_num,
                formatted_driver_num,
                owns_car_display,
                formatted_insurance_num,
            ) = format_employee_data(employee)

            # Printing the formatted data for the display.
            print("----------------------------------------")
            print()
            print(f"     Employee Insurance Information")
            print()
            print(f"   Insurance Company: {formatted_insurance_name:<25s}")
            print()
            print("----------------------------------------")
            print()
            print(f"  Driver Name:    {formatted_name:>20s}")
            print(f"  License Number:      {formatted_license_num:>15s}")
            print(f"  Driver Number:                  {
                  formatted_driver_num:>4s}")
            print(f"  Insurance Number:              {
                  formatted_insurance_num:>5s}")
            print()
            print(f"  Owns Car:                        {owns_car_display:>3s}")
            print()
            print("----------------------------------------")
            print()
            break
        print()
        print(f"{RED}  Data Entry Error - Driver not found, please try again.{RESET}")
        print()

    # Checking to see if the user wants to run the program again.
    while True:
        run_again = input(
            f"{RED}  Would you like to check another driver? (Y/N): {RESET}").upper()
        if run_again not in ["Y", "N"]:
            print()
            print(f"{RED}  Data Entry Error - Please enter Y or N.{RESET}")
            print()
            continue
        elif run_again == "Y":
            insurance_report(employee_data)
            break
        elif run_again == "N":
            FV.clear_terminal()
            print()
            print(f"{GREEN}  Thank you for using the Employee Insurance Report program.{RESET}")
            print()
            return
