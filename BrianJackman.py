# Enter a new driver
# by Brian Jackman
# 2024 04 01 - 2024 04 02

import FormatValues as FV
import readfiles as RF
import string

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"


# function for inputs and validations
def driver_input():
    (
        numNextTrans,
        numNextDriver,
        FEE_MONTHLY_STAND,
        FEE_RENT_DAY,
        FEE_RENT_WEEK,
        HST_RATE,
        datePrev,
    ) = RF.read_defaults_file()
    FV.clear_terminal()
    while True:

        # while True:
        #     print()
        #     DrivNum = input("Enter the driver number (####): ")
        #     if not DrivNum.isdigit() or not len(DrivNum) == 4:
        #         print()
        #         print(
        #             "  Data Entry Error - Driver number must contain 4 numbers. Please try again."
        #         )
        #         continue
        #     break

        while True:
            print()
            insurance_num = input(
                "Enter the driver's insurance policy number (########): "
            )
            if not insurance_num.isdigit() or len(insurance_num) != 8:
                print()
                print(
                    "  Data Entry Error - Insurance policy number must contain 8 numbers. Please try again."
                )
                continue
            break

        while True:
            print()
            DrivFirName = input("Enter the driver's first name: ").strip()
            DrivFirName = DrivFirName.title()
            if not DrivFirName.isalpha():
                print()
                print(
                    "  Data Entry Error - First name must contain only alphabetic characters. Please try again."
                )
                continue
            break

        while True:
            print()
            DrivLasName = input("Enter the driver's last name: ").strip()
            DrivLasName = DrivLasName.title()
            if not DrivLasName.isalpha():
                print()
                print(
                    "  Data Entry Error - Driver's last name must contain only alphabetic characters. Please try again."
                )
                continue
            break

        while True:
            allowed_char = set(" -'.,")
            print()
            DrivAddress = input("Enter the driver's address: ").title()
            if not all(
                char.isalpha()
                or char.isspace()
                or char.isdigit()
                or char in allowed_char
                for char in DrivAddress
            ):
                print()
                print(
                    "  Data Entry Error - Driver's address contains invalid characters."
                )
                continue
            break

        while True:
            print()
            allowed_char = set(" -'.,")
            driver_city = string.capwords(input("Enter the driver's city: "))
            if not all(
                char.isalpha() or char.isspace() or char in allowed_char
                for char in driver_city
            ):
                print()
                print("  Data Entry Error - Driver's city contains invalid characters.")
                continue
            break

        while True:
            print()
            province = input("Enter the customer's province (XX): ")
            validated_province = FV.validate_province(province)
            if validated_province:
                province = validated_province
                break
            print()
            print(f"  Data Entry Error - Please enter a valid province abbreviation.")

        while True:
            print()
            DrivPhonNum = input("Enter the driver's phone number (##########): ")
            validated_phone_num = FV.check_phone_num(DrivPhonNum)
            if len(validated_phone_num) != 14:
                print()
                print(f"  {validated_phone_num}")
                continue
            DrivPhonNum = validated_phone_num
            break

        while True:
            print()
            DrivLicNum = input("Enter the driver's licence number (7-8 characters): ")
            if not all(char.isalnum() for char in DrivLicNum):
                print()
                print(
                    "  Data Entry Error - Driver's license number must be a combination of letters and numbers. Please try again."
                )
                continue
            elif len(DrivLicNum) not in [7, 8]:
                print()
                print(
                    "  Data Entry Error - Driver's license number must be 7 or 8 letters or numbers. Please try again."
                )
                continue
            DrivLicNum = DrivLicNum.upper()
            break

        while True:
            print()
            DrivLicExpDate = input(
                "Enter the driver licence expiry date: (YYYY-MM-DD): "
            )
            validated_date = FV.check_date_future(DrivLicExpDate)
            if not DrivLicExpDate or DrivLicExpDate.isspace():
                print()
                print(
                    "  Data Entry Error - Driver's license expiry date cannot be blank. Please try again."
                )
                continue
            elif validated_date.startswith("Data Entry Error"):
                print()
                print(f"  {validated_date}")
                continue
            break

        while True:
            print()
            InsurComp = input(
                "Enter the insurance company they are insured with: "
            ).title()
            # Allowing spaces in the insurance company name:
            if not all(c.isalpha() or c.isspace() for c in InsurComp):
                print()
                print(
                    "  Data Entry Error - Driver's insurance company must contain only alphabetic characters. Please try again."
                )
                continue
            break

        while True:
            print()
            Rental = input("Do they need a rental car?(Y/N): ").upper()
            if not Rental in ["Y", "N"]:
                print()
                print("  Data Entry Error - Must select Y or N.")
                continue
            break

        default_balance = 0.00

        # Save inputs to data file
        with open("employees.txt", "a") as z:
            z.write(
                f"\n{numNextDriver},{insurance_num},{DrivFirName},{DrivLasName},{DrivAddress},{driver_city},{province},{DrivPhonNum},{DrivLicNum},{InsurComp},{Rental},{default_balance}"
            )
        numNextDriver += 1

        RF.write_defaults_to_file(
            "Defaults.dat",
            numNextTrans,
            numNextDriver,
            FEE_MONTHLY_STAND,
            FEE_RENT_DAY,
            FEE_RENT_WEEK,
            HST_RATE,
            datePrev,
        )

        print()
        print(f"{GREEN}  Data Saved.{RESET}")
        print()

        while True:
            print()
            RunAgain = input(
                "Would you like to enter another employee? (Y/N): "
            ).upper()
            if RunAgain not in ["N", "Y"]:
                print()
                print("  Data Entry Error - Must enter Y or N")
            FV.processing_blinker()
            break
        if RunAgain == "N":
            print()
            print("  Exiting program...")
            FV.processing_blinker()
            FV.clear_terminal()
            return  # Exit the function and return to the main program


# Enter company revenues
# by Brian Jackman
# 2024 04 02


# function for inputs and validations
def revenue_input():
    (
        numNextTrans,
        numNextDriver,
        FEE_MONTHLY_STAND,
        FEE_RENT_DAY,
        FEE_RENT_WEEK,
        HST_RATE,
        datePrev,
    ) = RF.read_defaults_file()
    FV.clear_terminal()
    while True:

        # while True:
        #     print()
        #     TransID = input("Enter the transaction ID (###): ")
        #     if not TransID.isdigit() or len(TransID) != 3:
        #         print()
        #         print(
        #             "  Data Entry Error - Transaction ID must be 4 numbers. Please try again."
        #         )
        #         continue
        #     break

        while True:
            print()
            DrivNum = input("Enter the driver number (####): ")
            if not DrivNum.isdigit() or not len(DrivNum) == 4:
                print()
                print(
                    "  Data Entry Error - Driver number must contain 4 numbers. Please try again."
                )
                continue
            break

        while True:
            print()
            TransDate = input("Enter the transaction date: (YYYY-MM-DD): ")
            validated_date = FV.check_date_past(TransDate)
            if not TransDate or TransDate.isspace():
                print()
                print(
                    "  Data Entry Error - Transaction date cannot be blank. Please try again."
                )
                continue
            elif validated_date.startswith("Data Entry Error"):
                print()
                print(f"  {validated_date}")
                continue
            break

        while True:
            print()
            allowed_char = set(" -'.,")
            TransDesc = input("Enter the transaction description: ").title()
            if not all(
                char.isalpha() or char.isspace() or char in allowed_char
                for char in TransDesc
            ):
                print()
                print(
                    "  Data Entry Error - Transaction description contains invalid characters."
                )
                continue
            break

        while True:
            print()
            TransTotal = input("Enter the transaction amount: ")
            if not all(char.isdigit() or char == "." for char in TransTotal):
                print()
                print(
                    "  Data Entry Error - Invalid character entered. Please try again."
                )
                continue
            pre_tax_amts = FV.get_hst_from_total(TransTotal)
            hst_total, cost_pre_tax = pre_tax_amts
            break

        # save inputs to data file
        y = open("revenue.txt", "a")
        y.write(
            f"\n{numNextTrans},{TransDate},{TransDesc},{DrivNum},{cost_pre_tax},{hst_total},{TransTotal}"
        )
        numNextTrans += 1
        RF.write_defaults_to_file(
            "Defaults.dat",
            numNextTrans,
            numNextDriver,
            FEE_MONTHLY_STAND,
            FEE_RENT_DAY,
            FEE_RENT_WEEK,
            HST_RATE,
            datePrev,
        )
        print()
        print(f"{GREEN}  Data Saved.{RESET}")
        print()

        while True:
            print()
            RunAgain = input(
                "Would you like to enter another revenue claim? (Y/N): "
            ).upper()
            if RunAgain not in ["N", "Y"]:
                print()
                print("  Data Entry Error - Must enter Y or N")
            FV.processing_blinker()
            break
        if RunAgain == "N":
            print()
            print("  Exiting program...")
            FV.processing_blinker()
            FV.clear_terminal()
            return numNextTrans  # Exit the function and return to the main program


# Enter company expenses
# by Brian Jackman
# 2024 04 02


# function for inputs and validations
def expenses_input(hst):
    FV.clear_terminal()
    while True:

        while True:
            print()
            InvoiceNum = input("Enter the invoice number (####): ")
            if not InvoiceNum.isdigit() and len(InvoiceNum) != 4:
                print()
                print("  Data Entry Error - Invoice number must contain 4 numbers.")
            break

        while True:
            print()
            DrivNum = input("Enter the driver number (####): ")
            if not DrivNum.isdigit() or not len(DrivNum) == 4:
                print()
                print("  Data Entry Error - Driver number must contain 4 numbers.")
                continue
            break

        while True:
            print()
            InvoiceDate = input("Enter the transaction date: (YYYY-MM-DD): ")
            validated_date = FV.check_date_past(InvoiceDate)
            if not InvoiceDate or InvoiceDate.isspace():
                print()
                print(
                    "  Data Entry Error - Invoice date cannot be blank. Please try again."
                )
                continue
            elif validated_date.startswith("Data Entry Error"):
                print(f"  {validated_date}")
                continue
            break

        while True:
            print()
            ItemNum = input("Enter the item number (###): ")
            if not ItemNum.isdigit() or len(ItemNum) != 3:
                print()
                print("  Data Entry Error - Item number must contain 3 numbers.")
                continue
            break

        while True:
            print()
            allowed_char = set(" -'.,")
            ItemDesc = input("Enter the item description: ").title()
            if not all(
                char.isalpha() or char.isspace() or char in allowed_char
                for char in ItemDesc
            ):
                print()
                print(
                    "  Data Entry Error - Item description contains invalid characters."
                )
            break

        while True:
            print()
            try:
                ItemQty = int(input("Enter the item quantity: "))
                if ItemQty <= 0 or ItemQty > 100:
                    print()
                    print(
                        "  Data Entry Error - Item quantity must be between 1 and 100."
                    )
                    continue
                break
            except ValueError:
                print("  Data Entry Error - Item quantity must be a number.")

        while True:
            print()
            try:
                item_cost = float(input("Enter the item cost: "))
                if item_cost <= 0:
                    print()
                    print("  Data Entry Error - Item cost caannot be $0.00.")
                break
            except ValueError:
                print()
                print("  Data Entry Error - Item cost must be a number.")
                continue

        # Calculations:
        item_subtotal = item_cost * ItemQty
        hst_total = item_subtotal * hst
        item_total = item_subtotal + hst_total

        formatted_subtotal = round(item_subtotal, 2)
        formatted_hst = round(hst_total, 2)
        formatted_total = round(item_total, 2)

        # save inputs to data file
        x = open("expenses.txt", "a")
        x.write(
            f"\n{InvoiceNum},{DrivNum},{InvoiceDate},{ItemNum},{ItemDesc},{item_cost},{ItemQty},{formatted_subtotal},{formatted_hst},{formatted_total}"
        )

        print()
        print(f"{GREEN}  Data Saved.{RESET}")
        print()

        while True:
            print()
            RunAgain = input(
                "Would you like to enter another expense claim? (Y/N): "
            ).upper()
            if RunAgain not in ["N", "Y"]:
                print()
                print("  Data Entry Error - Must enter Y or N")
            FV.processing_blinker()
            break
        if RunAgain == "N":
            print()
            print("  Exiting program...")
            FV.processing_blinker()
            FV.clear_terminal()
            return  # Exit the function and return to the main program
