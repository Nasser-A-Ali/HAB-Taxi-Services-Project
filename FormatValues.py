# Importing required modules.
import datetime
import FormatValues as FV
import time
import sys
import os

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"


def clear_terminal():
    """
    Clears the terminal screen.
    """
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def processing_blinker():
    """
    A short blinking statement to pause inbetween inputs to create a better flow for the user.
    """
    print()
    # Change to control number of 'blinks'
    for _ in range(2):
        print(f"{GREEN}    Processing...{RESET}", end="\r")
        # Pause for 0.3 seconds
        time.sleep(0.3)
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)


def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(float(DollarValue))

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(float(DollarValue))

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr


# Brian'a Additions to this file.

# Formatting & validating postal codes


def format_postal_code(postal_code):
    """
    Accepts a value that has already been validated through the check_post_code function and format it to X#X #X#.

    Returns a formatted postal code.
    """
    postal_code = postal_code.upper()
    formatted_postal_code = (
        postal_code[0]
        + postal_code[1]
        + postal_code[2]
        + " "
        + postal_code[3]
        + postal_code[4]
        + postal_code[5]
    )
    return formatted_postal_code


# Formatting & validating postal codes


def check_postal_code(postal_code):
    """
    Accepts a value and checks if it is a valid postal code in terms of character count, alphabetical characters,
    and numerical characters. Formats the postal code to the format "A1A 1A1".

    Returns a formatted postal code or an error message.
    """
    # Remove any non-alphanumeric characters from the postal code with filter and isalnum - very cool
    normalized_postal_code = "".join(filter(str.isalnum, postal_code))

    # Check if the normalized postal code has the correct length and format
    if len(normalized_postal_code) != 6:
        return "Data Entry Error (Invalid postal code) - Postal code must be 6 characters long. Please try again."
    elif not (
        normalized_postal_code[0].isalpha()
        and normalized_postal_code[2].isalpha()
        and normalized_postal_code[4].isalpha()
    ):
        return "Data Entry Error (Invalid postal code) - Postal code must have letters in the first, third, and fifth positions. Please try again."
    elif not (
        normalized_postal_code[1].isdigit()
        and normalized_postal_code[3].isdigit()
        and normalized_postal_code[5].isdigit()
    ):
        return "Data Entry Error (Invalid postal code) - Postal code must have digits in the second, fourth, and sixth positions. Please try again."
    else:
        # Insert space between the third and fourth characters to format the postal code
        formatted_postal_code = (
            f"{normalized_postal_code[:3]} {normalized_postal_code[3:]}"
        )
        return formatted_postal_code.upper()


# Formatting & validating phone numbers


def format_phone_num(phone_num):
    """
    Accepts a value that has already been validated through the check_phone_num function and format it to (###) ###-####.

    Returns a formatted phone number.
    """
    formatted_phone_num = f"({phone_num[0:3]}) {phone_num[3:6]}-{phone_num[6:10]}"
    return formatted_phone_num


# Formatting & validating phone numbers


def check_phone_num(phone_num):
    """
    Accepts a value and checks if it is a valid phone number in terms of character count and numerical characters.

    Returns a formatted phone number or an error message.
    """
    if len(phone_num) != 10:
        return "Data Entry Error (Invalid phone number) - Character count issue. Please try again."
    elif not phone_num.isdigit():
        return "Data Entry Error (Invalid phone number) - Phone number must only be numerical values. Please try again."
    phone_num = format_phone_num(phone_num)
    return phone_num


# Formatting & validatng dates to YYYY-MM-DD format.


def format_date(date):
    """
    Accepts a value that has already been validated through the check_date function and formats it to YYYY-MM-DD.

    Returns a formatted date.
    """
    formatted_date = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
    return formatted_date


# Validating dates in YYYY-MM-DD format.


def check_date_future(date):
    """
    Accepts a value and checks if it is a valid date in terms of character count,
    numerical characters, and valid date values. Also checks if the date is not in the future.

    Returns a formatted date or an error message.
    """
    if len(date) != 10:
        return (
            "Data Entry Error (Invalid date) - Date must be in the format YYYY-MM-DD."
        )
    elif not date[0:4].isdigit() or not date[5:7].isdigit() or not date[8:10].isdigit():
        return (
            "Data Entry Error (Invalid date) - Date must only contain numerical values."
        )
    else:
        try:
            year, month, day = map(int, date.split("-"))
            if datetime.datetime(year, month, day) < datetime.datetime.now():
                return "Data Entry Error (Invalid date) - Date cannot be past."
            return format_date(date)
        except ValueError:
            return "Data Entry Error (Invalid date) - Date values are out of range."


def check_date_past(date):
    """
    Accepts a value and checks if it is a valid date in terms of character count,
    numerical characters, and valid date values. Also checks if the date is not in the past.

    Returns a formatted date or an error message.
    """
    if len(date) != 10:
        return (
            "Data Entry Error (Invalid date) - Date must be in the format YYYY-MM-DD."
        )
    elif not date[0:4].isdigit() or not date[5:7].isdigit() or not date[8:10].isdigit():
        return (
            "Data Entry Error (Invalid date) - Date must only contain numerical values."
        )
    else:
        try:
            year, month, day = map(int, date.split("-"))
            if datetime.datetime(year, month, day) > datetime.datetime.now():
                return "Data Entry Error (Invalid date) - Date cannot be in the future."
            return format_date(date)
        except ValueError:
            return "Data Entry Error (Invalid date) - Date values are out of range."


# Validating province


def validate_province(province):
    """
    Accepts a value and checks if it is a valid province abbreviation, by using a list of valid province abbreviations.

    Returns the province abbreviation if valid, otherwise returns None.
    """
    PROVINCES = [
        "AB",
        "BC",
        "MB",
        "NB",
        "NL",
        "NS",
        "NT",
        "NU",
        "ON",
        "PE",
        "QC",
        "SK",
        "YT",
    ]
    province = province.upper()
    if province not in PROVINCES:
        return None
    else:
        return province.upper()


# Determine morning, afternoon, or evening based on time


def time_of_day(current_hour):
    """
    Accepts a time in 24-hour format

    Returns the time of day as morning, afternoon, or evening.
    """
    # Define the time ranges for morning, afternoon, and night
    # 6:00 AM to 11:59 AM
    morning_range = range(6, 12)
    # 12:00 PM to 5:59 PM
    afternoon_range = range(12, 18)
    # 6:00 PM to 11:59 PM
    night_range = range(18, 24)

    # Determine whether it's morning, afternoon, or night
    if current_hour in morning_range:
        return "morning"
    elif current_hour in afternoon_range:
        return "afternoon"
    elif current_hour in night_range:
        return "evening"
    else:
        return "night"


# Formatting percentages with 0 decimal places.


def format_perc_no_decimal(perc_value):
    """
    Accepts a value and formats it to a percentage with no decimal places.

    Returns a formatted percentage with no decimal places.
    """
    return "{:.0%}".format(perc_value)


# Formatting percentages with 1 decimal place.


def format_perc_one_decimal(perc_value):
    """
    Accepts a value and formats it to a percentage with one decimal place.

    Returns a formatted percentage with one decimal place.
    """
    return "{:.1%}".format(perc_value)


# Formatting percentages with 2 decimal places.


def format_perc_two_decimal(perc_value):
    """
    Accepts a value and formats it to a percentage with two decimal places.

    Returns a formatted percentage with two decimal places.
    """
    return "{:.2%}".format(perc_value)


def get_hst_from_total(total):
    """
    Accepts a total value of an item and returns the HST value (based on HST rate in Newfoundland and Labrador on April 9th, 2024).
    """
    HST_RATE = 0.15
    total = float(total)
    cost_pre_hst = total / (1 + HST_RATE)
    cost_pre_hst = round(cost_pre_hst, 2)
    hst_total = total - cost_pre_hst
    hst_total = round(hst_total, 2)

    return hst_total, cost_pre_hst


def FDateSFS(DateValue):
    if isinstance(DateValue, str):
        DateValue = datetime.datetime.strptime(DateValue, "%Y-%m-%d")
    return DateValue.strftime("%Y-%m-%d")


def format_dollar_values(*args):
    """
    Formats multiple values as dollar amounts (2 decimal places, $ in front).

    Arguments:
    *args: Any number of values can be formatted.

    Returns:
    A list of formatted values.
    """
    formatted_values = []
    for value in args:
        formatted_values.append(FV.FDollar2(value))
    return formatted_values
