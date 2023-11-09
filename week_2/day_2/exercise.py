# ITP Week 2 Day 2 Exercise

# import the appropriate method from the correct module
from openpyxl import Workbook, load_workbook
# Import the workbook that you updated in today's practice from
# "./spreadsheets/inventory.xlsx"

# relative path can run this program from VS Code (ctrl+F5)
# wb = load_workbook("week_2/spreadsheets/inventory.xlsx") 

# explicit path can allow this program to run from terminal: "$python3 exercise.py"
wb = load_workbook("/home/ra11y/Downloads/local.source/vetsInTech/week_2/spreadsheets/inventory.xlsx")
# access and store the appropriate worksheet to the variable 'ws'
sheet_name_list = wb.sheetnames
print(sheet_name_list)
ws = wb['CURRENT_MONTH_INVENTORY']

# Define a function called add_order_amount that takes in a single parameter called 'row'

# quantity_col = list(ws.columns)[4] # index value starts at 0 in python. 4 = column 'E'
# for quant_obj in quantity_col:
#     print(quant_obj.value)
    
# threshold_col = list(ws.columns)[3]
# for thresh_obj in threshold_col:
#     print(thresh_obj.value)

# max_amt_col = list(ws.columns)[2]
# for max_amt_obj in max_amt_col:
    # print(max_amt_obj.value)

# print(f"\nMax amount column output: {max_amt_col}\n")

def add_order_amount(row):
    quantity_col = list(ws.columns)[4] # index value starts at 0 in python. 4 = column 'E'
    for quant_obj in quantity_col:
        print(quant_obj.value)
    
    threshold_col = list(ws.columns)[3]
    for thresh_obj in threshold_col:
        print(thresh_obj.value)

    max_amt_col = list(ws.columns)[2]
    for max_amt_obj in max_amt_col:
        print(max_amt_obj.value)

    if quant_obj[row].value <= thresh_obj[row].value:
        order_amount = max_amt_obj[row].value - quant_obj[row].value
        ws.cell(row=row, column=6, value=order_amount) # by openpyxl column=6 = 'F'

    # IF the quantity is less or equal to than the threshold,
        # than calculate the order_amount (max_amount - quantity) 
        # assign the value to that row, column 6
# TIP: create variables for quantity, threshold, max_amount that retrieves the values first for cleanliness

# Perform a for..in loop through the range(2, len(inventory.rows))
#   - call the function add_order_amount() passing in the number of the range
# ws.cell(row=1, column=6, value='Inventory')
for rows in range(2, (ws.max_row)+1):
    add_order_amount(rows)
    