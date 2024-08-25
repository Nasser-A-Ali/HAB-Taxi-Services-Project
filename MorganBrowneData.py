# Analytics Data: Final Sprint.
# Morgan Browne

import FormatValues as FV


def generateAnalyticsData(revenue_data, employee_data, expenses_data):
    """
    This function will print some analytics data gathered from the arguments passed in.
    """
    # Initializing total expenses
    total_expenses = 0

    # Calculate total expenses
    for expense_record in expenses_data:
        total_expenses += float(expense_record["invoice_total"])

    total_expenses = 0
    for expense in expenses_data:
        total_expenses += float(expense["invoice_total"])

    earning_list = []

    for revenue in revenue_data:
        earning_list.append(
            {
                "driver_num": revenue["driver_num"],
                "revenue": float(revenue["transaction_total"]),
            }
        )

    driver_earnings = {}
    for earning in earning_list:
        driver_number = earning["driver_num"]
        revenue = earning["revenue"]
        if driver_number in driver_earnings:
            driver_earnings[driver_number] += revenue
        else:
            driver_earnings[driver_number] = revenue

    highest_earning_driver = max(driver_earnings, key=driver_earnings.get)
    highest_earning_revenue = driver_earnings[highest_earning_driver]

    total_employees = len(employee_data)

    average_expense_per_employee = total_expenses / total_employees

    formatted_total_expenses = FV.FDollar2(total_expenses)
    formatted_average = FV.FDollar2(average_expense_per_employee)
    formatted_highest_earning_revenue = FV.FDollar2(highest_earning_revenue)

    print()
    print()
    print(f"    Analytic Data: HAB TAXI SERVICES")
    print()
    print("============================================")
    print()
    print(f"  Total Expenses:               {formatted_total_expenses:>10s}")
    print(f"  Total Employees:                     {total_employees:>3d}")
    print()
    print("============================================")
    print()
    print(f"  Average Expense per Employee: {formatted_average:>10s}")
    print()
    print(f"  Total Revenue:                {formatted_highest_earning_revenue:>10s}")
    print()
    for employee in employee_data:
        if employee["driver_num"] == highest_earning_driver:
            formatted_name = f"{employee['first_name']} {employee['last_name']}"
            print(f"  Highest earning driver: {formatted_name:>16s}")
    print()
    print("============================================")
    print()
    # Calculate average expense per employee
    if len(employee_data) > 0:
        average_expense_per_employee = total_expenses / len(employee_data)
        formatted_average = FV.FDollar2(average_expense_per_employee)
        print(f"  Average Expense per Employee: {formatted_average:>10s}")
    else:
        print("No employees found. Hire someone!!")
    print()

    input("   Press Enter to return to the main program menu.")
    FV.clear_terminal()
    print()
