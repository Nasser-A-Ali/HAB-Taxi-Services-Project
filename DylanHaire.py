# Description: A function for HAB Taxi Services to update the revenue file and employee balance due entries at the start of each month.
# Author: Nasser Ali, Dylan Haire, Brian Janes
# Date(s): Apr. 04, 2024, Apr. 05, 2024; Apr. 08, 2024

# Import libraries
import datetime
import readfiles as RF

# Define program constants
DATE_MONTHLY_FEE = 1

# Define program variables
dateCur = datetime.datetime.now().date()


def updateStandFees():
    # Using readfiles.py to read Defaults.dat
    numNextTrans, numNextDriver, FEE_MONTHLY_STAND, FEE_RENT_DAY, FEE_RENT_WEEK, HST_RATE, datePrev = RF.read_defaults_file()

    # Return updated value for numNextTrans?
    # global numNextTrans
    transDesc = "Monthly Stand Fees"
    empDict = {}  # "numDriver": [], "hasOwnCar": []}
    empList = []
    revList = []
    dateCurMonth = dateCur.month
    dateCurYear = dateCur.year
    datePrevMonth = datePrev.month

    if dateCurMonth > datePrevMonth:
        print()
        print("Updating monthly stand fees...")
        print()
        # Transaction date - First day of the month
        dateTrans = datetime.datetime(
            dateCurYear, dateCurMonth, DATE_MONTHLY_FEE).date()

        # Calculate monthly stand fees, HST, and total cost
        costMnthStand = FEE_MONTHLY_STAND
        costMnthHST = costMnthStand * HST_RATE
        costMnthTotal = costMnthStand + costMnthHST

        # From "employees.txt," create a list of Driver IDs
        # Open "employees.txt" in "r+" mode, to read Driver IDs and (later) write employee balances
        with open("employees.txt", "r+") as fileEmp:
            # Skip the headers in employees.txt
            next(fileEmp)
            # Iterate over each line in "employees.txt"
            for line in fileEmp:
                # Create a list of entries in "employees.txt"
                empList = line.strip().split(",")
                # NOTE: empList only keeps the last entry when the 'for' loop finishes iterating, while the dictionary retains all its values
                # Get Driver IDs (empList[0]) and Car Ownership (empList[10])
                numDriver = empList[0]
                hasOwnCar = empList[10]
                # Create a dictionary linking Driver IDs and Car Ownership as key-value pairs
                empDict[numDriver] = hasOwnCar

        with open("revenue.txt", "a") as fileRev:
            # Next transaction number - imported from "Defaults.dat"
            # Iterate over each line in "empList"
            # Checks if the driver has their own car and calculates the monthly stand fees, the HST, and the total cost.

            for numDriver, hasOwnCar in empDict.items():
                if hasOwnCar == "Y":
                    # Create an f-string with required elements for "revenue.txt"
                    revData = f"\n{numNextTrans},{dateTrans},{transDesc},{
                        numDriver},{costMnthStand},{costMnthHST},{costMnthTotal}"
                    # Append transaction data to revList to create an entry
                    revList.append(revData)
                    # Increment the transaction number by 1 for the next transaction
                    numNextTrans += 1
                    
            # Write the list to "revenue.txt"
            fileRev.writelines(revList)

        # Updating the previous date to the current date if we paid the stand fees, to avoid duplicate charges.
        datePrev = dateCur
        # Update the "Defaults.dat" file with the new transaction number
        RF.write_defaults_to_file("Defaults.dat", numNextTrans, numNextDriver, FEE_MONTHLY_STAND, FEE_RENT_DAY, FEE_RENT_WEEK, HST_RATE, datePrev)

        print()
        print("Monthly stand fees updated successfully.")
        print("Employee balances to be updated.")
        print()
    else:
        print()
        print("Monthly stand fees already up-to-date!")
    return
