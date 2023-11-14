# ITP Week 3 Day 1 Practice

# import your required modules/methods
from openpyxl import Workbook, load_workbook
# given the following items, using the methods we covered, write to openpyxl
wb = Workbook()
ws = wb.active

# use an external counter with just a for loop (no function)

clefairy = {
    "id": 35,
    "name": "clefairy",
    "base_experience": 113,
    "height": 6,
    "order": 56,
    "weight": 75,
}
counter = 0 # initialize the counter
for num in range(1, len(clefairy)):
    ws.cell(row=1, column=num , value=clefairy['id'])
    ws.cell(row=1, column=num , value=clefairy['name'])
    ws.cell(row=1, column=num , value=clefairy['base_experience'])
    ws.cell(row=1, column=num , value=clefairy['height'])
    ws.cell(row=1, column=num , value=clefairy['order'])
    ws.cell(row=1, column=num , value=clefairy['weight'])

# create a function that takes in a pokemon
weedle = {
    "id": 13,
    "name": "weedle",
    "base_experience": 39,
    "height": 3,
    "order": 17,
    "weight": 32
}

# call the function with weedle!
def pokemon_fcn(weedle):
    ws.cell(row=1, column=1, value=weedle['id'])
    ws.cell(row=1, column=2, value=weedle['name'])
    pass

#
# wb.save('./spreadsheets/practice.xlsx')
# absolute path
wb.save('/home/ra11y/Downloads/local.source/vetsInTech/week_3/spreadsheets/w3_d1_practice.xlsx')