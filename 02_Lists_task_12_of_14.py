#Your code below:
'''
task1
We want to have a way to store all of our classroom test score data.

Using the provided table, create a two-dimensional list called class_name_test to represent the data. Each sublist in class_name_test should have one student’s name and their associated score.
'''
class_name_test = [["Jenny",90],["Alexus",85.5],["Sam",83],["Ellie",101.5]]
print(class_name_test)
'''
task2
Use double square brackets ([][]) to select Sam‘s test score from the list class_name_test.

Save it to the variable sams_score.

Print the variable sams_score to see the result.
'''
sams_score = class_name_test[2][1]
print("Sam's score: ")
print(sams_score)
'''
task3
Use double square brackets ([][]) to select Ellies test score from the list class_name_test. This time only use negative indices!

Save it to the variable ellies_score.

Print the variable ellies_score to see the result.
'''
ellies_score = class_name_test[-1][-1]
print("Ellis scrore: ")
print(ellies_score)