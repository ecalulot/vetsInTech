# notes from class

# dict      {"first_name": "Rick", "last_name":"Sanchez"}   ordered, changeable, no duplicates
# list      ["Rick", "Morty", "Summer"]                     ordered, changeable, allows duplicates
# tuple*    ("physics", "chemistry", 1997, 2000)            ordered, unchangeable, allows duplicates
# string    "hello"
# int       42
# float     42.42
# Boolean   True/False

import json
 
# json.dumps() # function converts a Python dictionary into a JSON.
 
example_dict = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ["Ann", "Billy"],
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(type(example_dict))

json_obj_output = json.dumps(example_dict)
print(json_obj_output)
print(type(json_obj_output))