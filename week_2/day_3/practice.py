# ITP Week 2 Day 3 (In-Class) Practice

# 1. 
    # a. run the following function and examine the behavior of the function return

def print_greeting():
    greetings = "hello"
    print(greetings)

# run it here!
# salutations = print_greeting()
# you are suppposed to do the following:

print(print_greeting())
# this will return 'None' as it is an implicit return

    # b. Convert this implicit return function to an explicit return function!

def return_greeting():
    greetings = "salutations"
    # CHANGE LINE BELOW
    return(greetings) # this is an explicit return so we can use it later by calling the fcn again
    # CHANGE LINE ABOVE

    # c. Run the newly printed code! (Examine NOTHING is printed to the terminal!)
return_greeting()
# run it here!
print(return_greeting())

    # d. Create a variable my_greeting and store the return value of return_hello then print the variable!
my_greeting = print_greeting()

print(my_greeting)

# # using a 'return' in a fcn is called an explicit return statement
# def return_42():
#     return 42 # forces the fcn to end 

# # we are explcitly returning something to the fcn called. this can then be later 
# # used further within the code.

# def return_42():
#     forty_two = 42
#     return forty_two

# print(forty_two) # program does not know 'forty_two' because it is out of scope

# def useReturn(forty_two): # this fcn is using the other fcn as its arguement
#     forty_two + 8 
#     print(forty_two + 8)


# useReturn(return_42()) # this will give us the forty_two we need

# # so the useReturn must use the other function as its arguement 

# def take_a_number(num):
#     return num ** num

# take_a_number(3)



# # printing a value is not the same as returning a value


import math
math. # call the fcn and add a dot ( . ) and vscode will show you all
# the other methods you can use that are associated with the main fcn


