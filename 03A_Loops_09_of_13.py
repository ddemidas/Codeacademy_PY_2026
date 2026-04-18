ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
'''
task1
Your computer is the doorman at a bar in a country where the drinking age is 21.
Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
'''
for age in ages:
  if age < 21:
    continue
  #this line gives a nice output but Codeacademy engine expects us to print out only digits as an output
  #print("The age of our visitors is: " + str(age))
  #so we are printing out outputs only
  print(age)