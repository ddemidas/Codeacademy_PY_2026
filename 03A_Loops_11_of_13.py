grades = [90, 88, 62, 76, 74, 89, 48, 57]
'''
task1
We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.
Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.
'''
scaled_grades = [grade + 10 for grade in grades]
print("Grades scaled: " + str(scaled_grades))
#again Codeacadey engine wants me to print out the variable explicitly
print(scaled_grades)