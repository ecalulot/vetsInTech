# ITP Week 1 Day 4 Exercise

# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element
for lett in lowercase:
    print(lett)

# 2. loop through the lowercase and print the capitalization of each element
for lett in lowercase:
    print(lett.upper())
    # these next two might work just because the list are single chars
    # print(lett.capitalize())
    # print(lett.title())

# MEDIUM

# # 1. create a new variable called uppercase with an empty list
# uppercase = []
# # 2. loop through the lowercase list

# # for lett in lowercase:
# #     # 2a. append the capitalization of each element to the uppercase list
# #     uppercase.append(lett.upper())
# # print(uppercase)
# for lett in lowercase:
#     uppercase.append(lett.upper())

# print(uppercase)


# pretty sure the above can be done in a list comprehension - relearn this.
uppercase = [lett.upper() for lett in lowercase]

# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

# password = "MySuperSafePassword!@34"
password = input("Hello user! Enter a password: ")

# added ' ' i.e. space character to the 'special_char' list
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']

# 1. create the following variables and assign them Booleans as False
    # has_uppercase
has_uppercase = False
    # has_lowercase
has_lowercase = False
    # has_number
has_number = False
    # has_special_char
has_special_char = False

# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

password_list = list(password)
for char in password_list:
    print(char)

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

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
# better version:
    # elif letter.isdigit():
    #     has_number = True
    #     continue
# continue is actually not necessary for the whole block of code
# might have to create an list of actual numbers to check against

# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

# final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop
# if final_result_shorthand == True:
#     print("Your password is safe and strong")
# else:
#     print("Update password: too weak")

# refactor using ternary operation for lines 92 - 95
print("Your password is safe and strong." if final_result_shorthand == True else print("Update password: too weak."))

# BONUS: update the password variable to take in an user input!
 # See line 34 for BONUS

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!
# should create line 112 into a block and add lines 119 - 127 under the failed weak password as a sub-block of code 
if final_result_shorthand == False:
    if has_uppercase != True:
        print("Your password is missing an uppercase.")       
    if has_lowercase != True:
        print("Your password is missing a lowercase.")
    if has_number != True:
        print("You are missing a number in your password.")       
    if has_special_char != True:
        print("You are missing a special character in the password")

# the 'if' statement will keep checking all 'if' statements without kicking you out of the loop.
# i should have remembered that from previous lessons. 


# refactor attempt to use list comprehension
# pw_reqs = [has_uppercase, has_lowercase, has_number, has_special_char]
# password_strength = [req != True for req in pw_reqs] 
# if password_strength == False:
#     print('Password is missing a requirement. Update password') 
# else: 
#     print('Your password has the proper requirements.')