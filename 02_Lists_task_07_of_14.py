'''
task1
Use square brackets ([ and ]) to access the 4th employee from the list employees. Save it to the variable employee_four.
'''
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four=employees[3]
print("employee_four: "+str(employee_four))
'''
task2
Paste the following code into script.py:
'''
#print(employees[8])
'''
Accessing an element that does not exist produces an IndexError.

In the line of code that you pasted, change 8 to an index that exists so that you don’t get an IndexError.

Run your code again!
'''
print(employees[6])
print("employees: "+str(employees))
