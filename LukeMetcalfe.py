    # Description: Program to print a report for HAB Taxi Services profit Listings.
# Author: Luke Metcalfe
# Date: April 2, 2024

# Import required libraries
import datetime
import FormatValues as FV

FormattedTodayDate = FV.FDateS(datetime.datetime.now())

def PrintCompanyProfitListing(revenue_data, expenses_data):
    FV.clear_terminal()
    # Perform required Calculations
    # Calculate total revenue
    TotalRevenue = 0
    for Record in revenue_data:
        TotalRevenue += float(Record["transaction_total"])

    # Calculate total expenses
    TotalExpenses = 0
    for Expense in expenses_data:
        TotalExpenses += float(Expense["invoice_total"])

    # Calculate profit/loss
    ProfitLoss = TotalRevenue - TotalExpenses

    # Formatting dollar values
    FormattedTotalRevenue = FV.FDollar2(TotalRevenue)
    FormattedTotalExpenses = FV.FDollar2(TotalExpenses)
    FormattedProfitLoss = FV.FDollar2(ProfitLoss)

    # Generate report headings
    print()
    print()
    print("      HAB TAXI SERVICES")
    print("      PROFIT LISTING REPORT")
    print()
    print("===================================================================================================================")
    print()
    print(f"    REVENUE TABLE:                                                              DATE: {FormattedTodayDate:>10s}")
    print()
    print()
    print("    TRANSACTION   DRIVER    TRANSACTION       TRANSACTION                  TRANSACTION  TRANSACTION  TRANSACTION")
    print("    ID            NUMBER    DATE              DESCRIPTION                  AMOUNT       HST          TOTAL")
    print("===================================================================================================================")
    print()
    for Record in revenue_data:
        print(f"      {Record["transaction_id"]:>3s}          {Record["driver_num"]:>4s}     {Record["transaction_date"]}        {Record["transaction_details"]:<25s}  {FV.FDollar2(Record["transaction_amount"]):>10s}  {FV.FDollar2(Record["transaction_hst"]):>10s}    {FV.FDollar2(Record["transaction_total"]):>10s}")
    print()
    print("===================================================================================================================")
    print()
    print(f"        TOTAL REVENUE: {FormattedTotalRevenue:>10s}")
    print()
    print("===================================================================================================================")

    print()
    input("Press Enter to continue to Expenses data.")
    FV.clear_terminal()

    print()
    print(f"    EXPENSES TABLE:                                                                                              DATE: {FormattedTodayDate:>10s}")
    print()
    print()
    print("     INVOICE    DRIVER       INVOICE      ITEM         ITEM       ITEM                          ITEM     INVOICE       INVOICE        INVOICE")
    print("     NUMBER     NUMBER       DATE         NUMBER       COST       DESCRIPTION                   QTY      SUBTOTAL      HST            TOTAL")
    print("   ============================================================================================================================================")
    print()
    for Expense in expenses_data:
        print(f"     {Expense["invoice_num"]:>6s}      {Expense["driver_num"]:>4s}      {Expense["invoice_date"]:<10s}      {Expense["item_num"]}    {FV.FDollar2(Expense["item_cost"]):>10s}      {Expense["item_desc"]:<30s} {Expense["item_quantity"]:>2s}   {FV.FDollar2(Expense["invoice_subtotal"]):>10s}    {FV.FDollar2(Expense["invoice_hst"]):>10s}     {FV.FDollar2(Expense["invoice_total"]):>10s}")
    print()
    print("   ============================================================================================================================================")
    print()
    print(f"        TOTAL EXPENSES: {FormattedTotalExpenses:>10s}")
    print()
    print(f"        PROFIT/LOSS: {FormattedProfitLoss:>10s}")
    print()
    print("   ============================================================================================================================================")
    print()
    input("Press Enter to continue to analytic data...")
    FV.clear_terminal()
