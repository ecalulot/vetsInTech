# ITP Week 2 Day 4 (In-Class) Practice

# Dictionary

# create a new dictionary named my_person with one key value pair of name : [YOUR_NAME]
my_person = {'efren': 'calulot'}

# verify the type of my_person to be a dictionary by using type
print(f"The 'my_person' variable is an object of type: {type(my_person)}\n")

# Next we will use a pre-made dictionary:

person_1 = {
    "first_name": "Scooby",
    "favorite_snack": "Rare Candy",
    "wears_glasses": True
    }

# add a key value pair to person_1 with the last_name of Doo
person_1['last name'] = 'Doo'
print(f"Updated the 'last_name' key of the 'person_1' dictionary: {person_1}\n")

# update person_1 favorite_snack to "Scooby Snacks"
person_1['favorite_snack'] = 'Scooby Snacks'
print(f"Altered the 'favorite_snack' key. The new dictionary is: {person_1}\n")

# Remove the "wears_glasses" key:value from person_1
