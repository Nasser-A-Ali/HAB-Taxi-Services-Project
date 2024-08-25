# Description: Main body for a program for HAB Taxi Services to handle employees, finances, and car rentals
# Author: Dylan Haire
# Date(s): Apr. 01, 2024; Apr. 02, 2024; Apr. 03, 2024; Apr. 04, 2024; Apr. 08, 2024

# Import libraries
import time
import BrianJanes as BJN
import BrianJackman as BJK
import DylanHaire as DH
import LukeMetcalfe as LM
import MorganBrowneData as MB
import readfiles as RF
import FormatValues as FV

# Load data from text files
# These are all lists of dictionaries that include the data we want from their respective files.
employee_list = RF.read_employee_file()
revenues_list = RF.read_revenue_file()
expenses_list = RF.read_expense_file()

# Define program constants.

feeMnthStandDay = 1


# Open Defaults.dat in "r+" mode to read and write without automatically overwriting
# fileDef = open("Defaults.dat", "r")
# numNextTrans = int(fileDef.readline())
# numNextDriver = int(fileDef.readline())
# FEE_MONTHLY_STAND = float(fileDef.readline())
# feeRentDay = float(fileDef.readline())
# feeRentWeek = float(fileDef.readline())
# HST_RATE = float(fileDef.readline())
# datePrev = datetime.datetime.strptime(fileDef.readline(), "%Y-%m-%d").date()

# fileDef.close()

# Define program functions.
# Call function to update monthly stand fees at program start
# nextNumTrans, datePrev = DH.updateStandFees(dateCur, datePrev, numNextTrans,
#                    FEE_MONTHLY_STAND, HST_RATE)

DH.updateStandFees()

(
    numNextTrans,
    numNextDriver,
    FEE_MONTHLY_STAND,
    FEE_RENT_DAY,
    FEE_RENT_WEEK,
    HST_RATE,
    datePrev,
) = RF.read_defaults_file()

# Defining threshold for bonus eligibility
THRESHOLD = 500

# Main program.
while True:

    # Gather user input.
    print()
    print("        HAB Taxi Services")
    print("     Company Services System")
    print()

    # List program options
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Print Driver Insurance Report.")
    print("9. Quit Program.")
    print()

    # Get an input from the user indicating their program choice (Validation - Must be 1-9)
    while True:
        try:
            choiceProg = input("Enter the desired program (1-9): ")
            choiceProg = int(choiceProg)

        except ValueError:
            print()
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        break

    # Perform required calculations
    # Select the function to run based on the user's input
    if choiceProg == 1:
        print()
        print("  Option 1 Selected")
        FV.processing_blinker()
        numNextDriver = BJK.driver_input()
    elif choiceProg == 2:
        print()
        print("  Option 2 Selected")
        FV.processing_blinker()
        numNextTrans = BJK.revenue_input()
    elif choiceProg == 3:
        print()
        print("  Option 3 Selected")
        FV.processing_blinker()
        BJK.expenses_input(HST_RATE)
    elif choiceProg == 4:
        FV.clear_terminal()
        print()
        print("  Option 4 Selected")
        print("  No Program Available.")
        time.sleep(2)
        FV.clear_terminal()
    elif choiceProg == 5:
        FV.clear_terminal()
        print()
        print("  Option 5 Selected")
        print("  No Program Available.")
        time.sleep(2)
        FV.clear_terminal()
    elif choiceProg == 6:
        print()
        print("  Option 6 Selected")
        FV.processing_blinker
        LM.PrintCompanyProfitListing(revenues_list, expenses_list)
        MB.generateAnalyticsData(revenues_list, employee_list, expenses_list)
    elif choiceProg == 7:
        FV.clear_terminal()
        print()
        print("  Option 7 Selected")
        print("  No Program Available.")
        time.sleep(2)
        FV.clear_terminal()
    elif choiceProg == 8:
        print()
        print("  Option 8 Selected")
        FV.processing_blinker()
        BJN.insurance_report(employee_list)
    elif choiceProg == 9:
        FV.clear_terminal()
        print()
        print("  Quitting program...")
        FV.processing_blinker()
        break
    else:
        print("Invalid input. Please enter a number between 1 and 9.")

# Any housekeeping duties at the end of the program.
# Write values back to Defaults.dat
# RF.write_defaults_to_file(
#     "Defaults.dat",
#     numNextTrans,
#     numNextDriver,
#     FEE_MONTHLY_STAND,
#     FEE_RENT_DAY,
#     FEE_RENT_WEEK,
#     HST_RATE,
#     datePrev,
# )
# Print a closing message for the user
print()
print("Thank you for using HAB Taxi Services!")
