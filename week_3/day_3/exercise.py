# ITP Week 3 Day 3 Exercise

# RICK AND MORTY API DOCS: https://rickandmortyapi.com/documentation

# we want to make a copy of the Rick and Morty database (which is provided through the api)


# EASY MODE

# import the appropriate modules (you have 3)
from openpyxl import Workbook, load_workbook
import json, requests

character_url = "https://rickandmortyapi.com/api/character"
# set up a workbook and worksheet titled "Rick and Morty Characters"
wb = Workbook()
ws = wb.active
ws.title = "Rick and Morty Characters"

# # assign a variable 'data' with the returned GET request
data = requests.get(character_url)
# create the appropriate headers in openpyxl for all of the keys for a single character
ws.cell(row=1, column=SOMECHARS.keys())
# loop through all of the 'results' of the data to populate the rows and columns for each character
def character_data(url_data):
    for col in range(1, len(data.keys())+1):
        ws.cell(row=2, column=col, value=list(data.values())[col-1])

character_data(data)
# NOTE: due to the headers, the rows need to be offset by one!

# MEDIUM MODE

# create 2 new worksheets for "Rick and Morty Locations" and "Rick and Morty Episodes"
ws.title = "Rick and Morty Locations"
ws.title = "Rick and Morty Episodes"

# create 2 new variables for episode_url and location_url (retrieve it from the docs!)
location_url = "https://rickandmortyapi.com/api/location"
episode_url = "https://rickandmortyapi.com/api/episode"

# populate the new worksheets appropriately with all of the data!
data_location = requests.get(location_url)
data_episode = requests.get(episode_url)

# NOTE: don't forget your headers!

# HARD MODE
# Can you decipher the INFO key of the data to use "next" url to continuously pull data?
# Currently, we are only pulling 20 items per api pull!
# WE WANT EVERYTHING. (contact instructors for office hours if stuck!)

# NIGHTMARE
# The inner information for characters, locations, and episodes, references one another through urls
# ie. for episode 28, it lists all the character but by their url
# can you use the URLs to make a subsequent call inside your for loops
# to replace the url with just the appropriate names?
# NOTE: need to make use of if statements to see if url exists or not
# (contact instructors for office hours if stuck!)


# wb.save("./spreadsheets/exercise.xlsx")
wb.save("/home/ra11y/Downloads/local.source/vetsInTech/week_3/w3_d3_spreadsheets")
# absolute path