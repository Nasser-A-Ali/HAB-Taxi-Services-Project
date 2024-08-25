# DESCRIPTION: Writing functions to read files, and save the data to a list of dictionaries.
# AUTHOR: Brian Janes
# DATE: April 4th, 2024

### I think that this could be useful for us to have access to in the main part of the program - so that any function that will need to read this information can have access to it if it's passed into the function as ann argument.

import datetime


def read_employee_file():
    """
    This function will open the revenue.txt file and read the data into a list of dictionaries.
    Returns a list of dictionaries with employee data.
    """
    employee_data = []
    with open("employees.txt", "r") as e:
        # Doing this to skip the first line which is currently headers.
        next(e)
        for line in e:
            # stripping the line, and splitting at the commas to create a list of values.
            employee_list = line.strip().split(",")
            # Appending the data to the employee_data list as a dictionary.
            employee_data.append(
                {
                    "driver_num": employee_list[0].strip(),
                    "insurance_num": employee_list[1].strip(),
                    "first_name": employee_list[2].strip(),
                    "last_name": employee_list[3].strip(),
                    "address": employee_list[4].strip(),
                    "city": employee_list[5].strip(),
                    "province": employee_list[6].strip(),
                    "phone_num": employee_list[7].strip(),
                    "license_num": employee_list[8].strip(),
                    "insurance_company": employee_list[9].strip(),
                    "own_car": employee_list[10].strip(),
                    "balance": employee_list[11].strip(),
                }
            )
        return employee_data


def read_revenue_file():
    """
    This function will open the revenue.txt file and read the data into a list of dictionaries.
    Returns a list of dictionaries with revenue data.
    """
    revenue_data = []
    with open("revenue.txt", "r") as r:
        # Doing this to skip the first line which is currently headers.
        next(r)
        for line in r:
            # stripping the line, and splitting at the commas to create a list of values.
            revenue_list = line.strip().split(",")
            # Appending the data to the revenue_data list as a dictionary.
            revenue_data.append(
                {
                    "transaction_id": revenue_list[0].strip(),
                    "transaction_date": revenue_list[1].strip(),
                    "transaction_details": revenue_list[2].strip(),
                    "driver_num": revenue_list[3].strip(),
                    "transaction_amount": revenue_list[4].strip(),
                    "transaction_hst": revenue_list[5].strip(),
                    "transaction_total": revenue_list[6].strip(),
                }
            )
        return revenue_data


def read_expense_file():
    """
    This function will open the expenses.txt file and read the data into a list of dictionaries.
    Returns a list of dictionaries with expense data.
    """
    expense_data = []
    with open("expenses.txt", "r") as x:
        # Doing this to skip the first line which is currently headers.
        next(x)
        for line in x:
            # stripping the line, and splitting at the commas to create a list of values.
            expense_list = line.strip().split(",")
            # Appending the data to the expense_data list as a dictionary.
            expense_data.append(
                {
                    "invoice_num": expense_list[0].strip(),
                    "driver_num": expense_list[1].strip(),
                    "invoice_date": expense_list[2].strip(),
                    "item_num": expense_list[3].strip(),
                    "item_desc": expense_list[4].strip(),
                    "item_cost": expense_list[5].strip(),
                    "item_quantity": expense_list[6].strip(),
                    "invoice_subtotal": expense_list[6].strip(),
                    "invoice_hst": expense_list[7].strip(),
                    "invoice_total": expense_list[8].strip(),
                }
            )
        return expense_data


def read_defaults_file():
    """
    This function will open the Defaults.dat file and read the data into a list of values.
    Returns a list of values with default data.
    """
    # Open Defaults.dat in "r+" mode to read and write without automatically overwriting
    fileDef = open("Defaults.dat", "r")
    numNextTrans = int(fileDef.readline())
    numNextDriver = int(fileDef.readline())
    FEE_MONTHLY_STAND = float(fileDef.readline())
    FEE_RENT_DAY = float(fileDef.readline())
    FEE_RENT_WEEK = float(fileDef.readline())
    HST_RATE = float(fileDef.readline())
    datePrev = datetime.datetime.strptime(fileDef.readline(), "%Y-%m-%d").date()

    fileDef.close()

    return (
        numNextTrans,
        numNextDriver,
        FEE_MONTHLY_STAND,
        FEE_RENT_DAY,
        FEE_RENT_WEEK,
        HST_RATE,
        datePrev,
    )


def write_defaults_to_file(
    filename,
    numNextTrans,
    numNextDriver,
    FEE_MONTHLY_STAND,
    FEE_RENT_DAY,
    FEE_RENT_WEEK,
    HST_RATE,
    datePrev,
):
    with open(filename, "w") as fileDef:
        defData = f"{numNextTrans}\n{numNextDriver}\n{FEE_MONTHLY_STAND}\n{FEE_RENT_DAY}\n{FEE_RENT_WEEK}\n{HST_RATE}\n{datePrev}"
        fileDef.write(defData)
