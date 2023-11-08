# ITP Week 2 Day 2 (In-Class) Practice 1
# 
# You will continue to work on the inventory spreadsheet that you created from yesterday's exercise
# import the appropriate method from the correct module
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string

wb = load_workbook("week_2/spreadsheets/inventory.xlsx")

# Import the workbook that you created in yesterday's exercise from
# "./spreadsheets/inventory.xlsx"

# verify what sheet names are available
print(wb.sheetnames)

# access and store the appropriate worksheet to the variable 'ws'
ws = wb.sheetnames
# Print out the cell values for each row

# Create a new column within that worksheet called order_amount
wb.insert_cols = ['len(max_column(wb)) + 1']
# save the latest changes
# wb.save("./spreadsheets/inventory.xlsx")