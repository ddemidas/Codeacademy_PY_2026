#Your code below:
'''
task1
Our school is expanding! We are welcoming a new set of students today from all over the world.

Using the provided table, create a two-dimensional list called incoming_class to represent the data. Each sublist in incoming_class should contain the name, nationality, and grade for a single student.
'''
'''
task2
"Madison" passed an exam to advance a grade. She will be pushed into 8th grade rather than her current 7th in our list.

Modify the list using double brackets [][] to make the change. Use positive indices.

Print incoming_class to see our change.
'''
incoming_class = [["Kenny", "American", 9],["Tanya", "Ukrainian", 9],["Madison", "Indian", 7]]
print("Incoming class students are: ")
print(incoming_class)
incoming_class[2][2]=8
print(incoming_class)
'''
task3
"Kenny" likes to be called by his nickname "Ken". Modify the list using double brackets [][] to accommodate the change but only using negative indices.

Print incoming_class to see our change.
'''

print(str(incoming_class[-3][-3]))

incoming_class[-3][-3]="Ken"
print(str(incoming_class[-3][-3]))
print(incoming_class)