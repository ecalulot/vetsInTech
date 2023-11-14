# ITP Week 3 Day 1 Practice

# import your required modules/methods
from openpyxl import Workbook, load_workbook
# given the following items, using the methods we covered, write to openpyxl
wb = Workbook()
ws = wb.active

# use an external counter with just a for loop (no function)
counter = 0 # initialize the counter
clefairy = {
    "id": 35,
    "name": "clefairy",
    "base_experience": 113,
    "height": 6,
    "order": 56,
    "weight": 75,
}


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


# wb.save('./spreadsheets/practice.xlsx')
# absolute path
wb.save('/home/ra11y/Downloads/local.source/vetsInTech/week_3/spreadsheets/practice.xlsx')