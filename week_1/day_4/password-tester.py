lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = [lett.upper() for lett in lowercase] # list comprehension
# for lett in lowercase:
#     uppercase.append(lett.upper())

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password = input("Hello user! Enter a password: ")
# password = "MySuperSafePassword!@34"

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False

password_list = list(password)
for char in password_list:  
    if char in lowercase:
        has_lowercase = True
        continue
    elif char in uppercase:
        has_uppercase = True
        continue
    elif char in special_char:
        has_special_char = True
        continue
    elif int(char) in list(range(0,10)):
        has_number = True
        continue

final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
    
if final_result_shorthand == True:
    print("Your password is safe and strong.\n")
else:
    print("Update password: too weak.\n")
    # password = input("Enter a stronger password: ")

# missing_reqs = []
if final_result_shorthand == False:
    if has_uppercase != True:
        # missing_reqs.append('uppercase')
        print("Your password is missing an uppercase.")
    if has_lowercase != True:
        # missing_reqs.append('lowercase')
        print("Your password is missing a lowercase.")
    if has_number != True:
        # missing_reqs.append('number')
        print("You are missing a number in your password.")
    if has_special_char != True:
        # missing_reqs.append('special character')
        print("You are missing a special character in the password")

# This code block works. 
#     print("\nYou are missing the following password requirement(s), at least one \
# of the following: ")
#     print(missing_reqs[:])
# kind of messy output as it puts the list items in quotes

# the 'if' statement will keep checking all 'if' statements without kicking you out of the loop.
# i should have remembered that from previous learnings. 
