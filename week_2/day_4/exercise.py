# ITP Week 2 Day 4 Exercise
import random

# 1. Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

# SCENARIO: A person came in and bought one of everything!

# for item in inventory:
    # decrement item by using an assignment operator
for k, v in inventory.items():
    if v <= 0: # for the case of nothing in stock to sell
        print(k, v)
    else: 
        v -= 1
        print(k, v)

    # NOTE: recall that item represents the key of the key:value pair


# 2. Implicit Functions 
# (When we work with global variables/objects and don't return anything, 
# these functions are implicit return functions!)
   

    # a. Dictionaries - create a function that takes in a dictionary which updates the "role" key value pair and makes it uppercase

user_1 = {
    "firstName": "Stephanie",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "95485"
    }

user_2 = {
    "firstName": "Brion",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "67344"
    }

user_3 = {
    "firstName": "Daniel",
    "lastName": "Kim",
    "role": "Instructor",
    "id": "74324"
    }

def alter_dict(user_dict):
    for k, v in user_dict.items():
        if 'role' in user_dict.keys():
            # user_dict['role']: str = v.upper()
            user_dict['role'] = 'INSTRUCTOR'
        else:
            v = v
    print(f"\nThe updated dictionary: {user_dict}\n")
    print(f"The memory address of 'user_dict' is: {id(user_dict)}.\n") # id prints memory address
    
# user_dict = input("\nGreetings programs! Enter a dictionary (user_1, user_2, or user_3): ")

    # b. Dictionaries - Run the functions (3 times for each user!)
alter_dict(user_3)
alter_dict(user_2)
# alter_dict(user_1)

instructor_list = [user_1, user_2, user_3]
# print(instructor_list)
print(f"The length of 'instructor_list is: {len(instructor_list)}\n")

    # c. List - create a function that takes in the list and 
    # checks if the each user's role is equal to "INSTRUCTOR". 
    # if it is the same, print VALID else print INVALID (try to use a loop here!)
def role_validation(instructor_list):
    for user in instructor_list:
        user_role = [print(f"VALID for {user['firstName']}.\n") if 'INSTRUCTOR' in user.values() else print(f"INVALID for {user['firstName']}.\n")]
        # print(user_role)

# role_check(instructor_list)
role_validation(instructor_list)


    # d. import the random module and update the function to re-assign the id of each user
for entry in len(instructor_list):
    for instructor_list[entry] in instructor_list:
        if instructor_list[entry] in instructor_list[entry].values():
            instructor_list[entry]['id'] = str(random.randint(10_000, 99_999))
            print(instructor_list)
    

    # for uval in user_2.values():
    # if 'id' in user_2.keys():
        # user_2["id"] = str(random.randint(10_000, 99_999))
        # print(uval)
    # e. don't forget to run it!
    
# 3. Explicit Functions
user_info = [46453, "Devin", "Smith"]
    # Each element by index of user_info follows the format of: id, first_name, last_name

    # Create a function with a parameter user_list
    #   - return a dictionary with the follow key value pairs:
    #   - id: user_list[0]
    #   - first_name: user_list[1]
    #   - last_name: user_list[2]