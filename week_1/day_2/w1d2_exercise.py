# ITP Week 1 Day 2 Exercise

# We will replicate a number magic trick with Python! Below is the magic trick that we will convert! Below that is the python instructions, you will need to complete.

# Step 1: Pick a number from 1 - 9
# Step 2: Multiple by 2
# Step 3: Add 10 to the total
# Step 4: Divide by 2
# Step 5: Subtract by the original number
# Final Number: 5

# assign a variable "step_1" to a number of your choice between 1 - 9
my_numb = 8

# assign a variable "step_2" to the product of step_1 and the number 2
double_numb = my_numb * 2

# assign a variable "step_3" to the sum of step_2 and the number 10
plus_ten = double_numb + 10

# assign a variable "step_4" to the quotient of step_3 and the number 2
cut_in_half = plus_ten / 2
# can use floor operator 'cut_in_half = plus_ten // 2' to use only the 
# quotient and not have to worry about the answer being a float

# assign a variable "step_5" to the difference between step_4 and step_1
final_val = cut_in_half - my_numb

# print step_5 and you should see 5!
print(f'\nThe magic number is {final_val}, TADA!\n')

# BONUS 1: can you convert step_1 to prompt a user's input?
# HINT: you need to cast step_1 to a int because user input is a type string.
new_numb = int(input('Enter a number from 1 - 9: '))

# BONUS 2: can you REFACTOR using less variables?
final_output = ((((new_numb * 2) + 10 ) / 2) - new_numb)
print(f"\nYour new magic number is: {final_output}, voila!")
# same as above: use the floor operator // to make keep the output an integer
# rather than a float. pretty smart to do so. 