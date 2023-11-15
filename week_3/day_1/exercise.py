# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]

# # list_to_dict = [{}]
# list_to_dict = {}
# for id, name in enumerate(users_list):
    # list_to_dict[id] = name # use 'id' as the key and set it to the value of 'name' as we enumerate
#     list_to_dict['user_id'] = id
#     list_to_dict['name'] = name
# print(list_to_dict) # strictly a single dictionary with 6 entries
# proper = [{k:v} for k,v in enumerate(users_list)]
# FOUND SO MANY OTHER WAYS THIS WAS NOT WORKING AND TESTED - TOO MANY TO KEEP HERE FOR FUTURE REFERENCE

# Properly done
list_to_dict = [{'user_id':k, 'name':v} for k,v in enumerate(users_list)]
print(list_to_dict)

# # 1a. Create a function that takes a single string value and returns the desired dictionary
def desired_dict(users_input):
    return(list_to_dict[users_input])

request_dict = int(input("\nEnter dictionary index to retrieve (0 - 6): "))
print(f"\nYou requested the following dictionary: {desired_dict(request_dict)}\n")


# 1b. Create a new empty list called users_dict_list
users_dict_list = []
# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list
for id, user in enumerate(users_list):
    # desired_dict(user==id)
    users_dict_list.append(desired_dict(user==id))
    # list_entry.insert(id, list_entry)
print(users_dict_list)
    # print(list_entry)


# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data
# 2a. retrieve the gender of Morty Smith
# print(mock_data['results'][1]['name']) # sanity check to test if I am in the correct dictionary and index
gender = mock_data['results'][1]['gender']
print(f"\nMorty is a {gender}.")
# 2b. retrieve the length of the Rick Sanchez episodes
num_episodes = len(mock_data['results'][0]['episode'])
print(f"Rick has been in {num_episodes} episodes thus far.")
# num_episodes_summer = len(mock_data['results'][2]['episode'])
# print(num_episodes_summer)
# 2c. retrieve the url of Summer Smith location
where_summer = mock_data['results'][2]['location']['url']
print(f"Summer is at {where_summer}")