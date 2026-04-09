last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
'''
task1
Create a list called subjects and fill it with the classes you are taking:

"physics"
"calculus"
"poetry"
"history"
'''
subjects = ["physics", "calculus", "poetry", "history"]
print("Subjects are: ")
print(subjects)
'''
task2
Create a list called grades and fill it with your scores:

98
97
85
88
'''
grades=[98, 97, 85, 88]
print("Grades are: ")
print(grades)
'''
task3
Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.
'''
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]
print("Gradebook is: ")
print(gradebook)
'''
task4
Print gradebook.
Does it look how you expected it would?
'''
'''
task5

Your grade for your computer science class just came in! You got a perfect score, 100!

Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.
'''
gradebook.append(["computer science", 100])
print("Gradebook is: ")
print(gradebook)
'''
task6
Your grade for "visual arts" just came in! You got a 93!
Use append to add ["visual arts", 93] to gradebook.
'''
gradebook.append(["visual arts", 93])
print("Gradebook is: ")
print(gradebook)
'''
task7
Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.

Access the index of the grade for your visual arts class and modify it to be 5 points greater.
'''
#a hint from AI code review:
'''
Accessing gradebook[5][1] assumes a fixed position; consider computing the index dynamically or validating before assignment to avoid potential errors if the list length changes.
'''
print(len(gradebook))
gradebook[len(gradebook)-1][1]=gradebook[len(gradebook)-1][1]+5
print("Gradebook is: ")
print(gradebook)
'''
task8
You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.

Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.
'''
gradebook.remove(["poetry", 85])
print("Gradebook is: ")
print(gradebook)
'''
task9
Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
'''
gradebook.append(["poetry","Pass"])
print("Gradebook is: ")
print(gradebook)

'''
task10
You also have your grades from last semester, stored in last_semester_gradebook.

Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.

Print full_gradebook to see our completed list.
'''
print("Last semester grades are: ")
print(last_semester_gradebook)
full_gradebook=last_semester_gradebook + gradebook
print("Full Gradebook is: ")
print(full_gradebook)