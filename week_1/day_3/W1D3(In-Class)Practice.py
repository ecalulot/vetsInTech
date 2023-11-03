# ITP Week 1 Day 3 (In-Class) Practice

# Take a look at the example codes below and determine their boolean value.

# ```python
a = 7//3
b = 2
a == b
# ```

Answer: True 

# ```python
c = 5
d = 10/2
c != d
# ```

Answer: True #(wrong) this is False

# ```python
e = 1
f = 10/10
e > f
# ```

Answer: False

# ```python
g = .5
h = 2/4
g <= h
# ```

Answer: True

# ```python
i = 5
i == 5.0
# ```

Answer: False #(wrong) this is True

# ```python
c >= i and e >= g
# ```
5 >= 5 and 1 >= .5
Answer: False #this is True

# ```python
c >= i or e >= g
# ```

Answer: True

# ```python
i*e == c and False
# ```
5 * 1 == 5 and False
Answer: False

# ```python
i*e > c or False
# ```
5 * 1 > 5
Answer: False

## Extra Time?

# Take two user INPUTs into two separate variable and PRINT the COMPARISON if they are both EQUAL

# ```python
# Code below here
value_one = int(input('Enter a number: '))
value_two = int(input('Enter your second number: '))
if value_one >= value_two:
    print('Your first number is larger.')
if value_one <= value_two:
    print('Your second number is larger.')
if value_one == value_two:
    print('Your two values match!')

# ```