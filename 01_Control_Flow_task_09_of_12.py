'''
1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

not (4 + 5 <= 9)

Copy to Clipboard

Statement two:

not (8 * 2) != 20 - 4
'''
statement_one = False

statement_two = True

'''
2.
The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you.

They want you to return to a previous if statement and add in several checks using and and not statements:

If a student’s credits is not greater or equal to 120, it should print:
"You do not have enough credits to graduate."

Copy to Clipboard

If their gpa is not greater or equal to 2.0, it should print:
"Your GPA is not high enough to graduate."

Copy to Clipboard

If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0, it should print:
"You do not meet either requirement to graduate!"

Copy to Clipboard

Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!
'''

credits = 120
gpa = 1.8

if not(credits>=120):
  print("You do not have enough credits to graduate.")
if not(gpa>=2.0):
  print("Your GPA is not high enough to graduate.")
if (not(credits>=120)) and (not(gpa>=2.0)):
  print("You do not meet either requirement to graduate!")
