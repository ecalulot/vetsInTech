# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]
# users_dict = {}
def list_of_dict(list_of_names):
    for id, user in enumerate(users_list):
        return [
            {'user_id': id, 'name': user },
    #   {'user_id': id, 'name': user }
    ]
    print(id, user)

print(enumerate(users_list))

# # 1a. Create a function that takes a single string value and returns the desired dictionary
# def desired_dict(users_input):
#     request_dict = dict(input("Enter dictionary in question: "))
#     return(request_dict)

# 1b. Create a new empty list called users_dict_list
users_dict_list = []
# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list
# for user in users_list:
#     desired_dict(user)
    # users_dict_list.append(???)
# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data
# 2a. retrieve the gender of Morty Smith
print(mock_data['results'][1]['name']) # test if I am in the correct dictionary and index
gender = mock_data['results'][1]['gender']
print(f"Morty is a {gender}.")
# 2b. retrieve the length of the Rick Sanchez episodes
num_episodes = len(mock_data['results'][0]['episode'])
print(f"Rick has been in {num_episodes} episodes thus far.")
num_episodes_summer = len(mock_data['results'][2]['episode'])
print(num_episodes_summer)
# 2c. retrieve the url of Summer Smith location
where_summer = mock_data['results'][2]['location']['url']
print(f"Summer is at {where_summer}")