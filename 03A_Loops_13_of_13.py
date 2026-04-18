# Your code below:
'''
task1
Create a list called single_digits that consists of the numbers 0-9 (inclusive).
'''
digit = 0
single_digits = range(10)
single_digits = [digit for digit in single_digits]
print(single_digits)

'''
task2
Create a for loop that goes through single_digits and prints out each one.
'''
for single_digit in single_digits:
  print(single_digit)

'''
task3
Before the loop, create a list called squares. Assign it to be an empty list to begin with.
'''
'''
task4
nside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
'''
'''
task5
After the for loop, print out squares.
'''
squares = []
for single_digit in single_digits:
  squares.append(single_digit**2)
print(squares)
'''
task6
Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
'''
'''
task7
Print cubes
'''
cubes = []
for single_digit in single_digits:
  cubes.append(single_digit**3)
print(cubes)