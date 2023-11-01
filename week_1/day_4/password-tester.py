lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = []
for lett in lowercase:
        uppercase.append(lett.upper())

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password = input("Hello user! Enter a password: ")

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
    elif int(char) in list(range(1,10)):
        has_number = True
        continue

final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
    
if final_result_shorthand == True:
    print("Your password is safe and strong")
else:
    print("Update password: too weak")
    # password = input("Enter a stronger password: ")
# probably use a while loop want to set it 'while final_result_shorthand = False' DO the loop, until True

if final_result_shorthand == False:
    if has_uppercase != True:
        print("Your password is missing an uppercase.")
    elif has_lowercase != True:
        print("Your password is missing a lowercase.")
    elif has_number != True:
        print("You are missing a number in your password.")
    elif has_special_char != True:
        print("You are missing a special character in the password")
