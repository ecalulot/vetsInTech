# ITP Week 3 Day 2 Practice

# 1. import the appropriate module
import json

json_1 = """
{
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
}
"""

# 2. perform a deserialization of the above object
decode_json_1 = json.loads(json_1)
print(decode_json_1)
print(type(decode_json_1)) # <class dict> as opposed to json


# 3. assign a new variable called url_1 to the value of the deserialized object's url
url_1 = decode_json_1['url']
# should be url_1 = decode_jason['url']


json_2="""
[
{
"albumId": 1,
"id": 1,
"title": "accusamus beatae ad facilis cum similique qui sunt",
"url": "https://via.placeholder.com/600/92c952",
"thumbnailUrl": "https://via.placeholder.com/150/92c952"
},
{
"albumId": 1,
"id": 2,
"title": "reprehenderit est deserunt velit ipsam",
"url": "https://via.placeholder.com/600/771796",
"thumbnailUrl": "https://via.placeholder.com/150/771796"
}
]
"""

# 4. deserialize and assign a variable url_2 with the second item's url
decode_json_2 = json.loads(json_2)
print(type(decode_json_2))
url_2 = decode_json_2[1]['url']
# probably should be decode_json_2[1]['url']
print(url_2)



# deserialization method does not require an import
# data = response.json() # built-in to python
# print(data)

# for post in data:
#     print(post['title'])

# must deserialize (decode/read) before accessing it
# get put post delete - these are the CRUD methods for requests