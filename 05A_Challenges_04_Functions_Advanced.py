'''
Challenges
We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills!
 '''
 
 '''
 1. First Three Multiples
Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. For this, we are going to need a few steps:

Define the function header to accept one input parameter called num
Print out 1 times num
Print out 2 times num
Print out 3 times num
Return the value of 3 times num
 '''
 '''
 Write a function named first_three_multiples() that has one parameter named num.

This function should print the first three multiples of num. Then, it should return the third multiple.

For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

Hint
For this function, we need to print() out the results of each multiplication * then return a single value. For example, printing the result of 3 times 5 would look like print(3 * 5) and returning it would look like return 3 * 5.
 '''
 # Write your first_three_multiples function here
def first_three_multiples(num):
  steps = [1, 2, 3]
  triangle = num * 3
  for i in steps:
    print(num*i)
  return triangle

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
#first_three_multiples(0)
# should print 0, 0, 0, and return 0
'''
2. Tip
Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. In order to do this, we will need a few steps:

Define the function to accept the total cost of the food called total and the percentage to tip as percentage
Calculate the tip amount by multiplying the total and percentage and dividing by 100
Return the tip amount
'''
'''
Create a function called tip() that has two parameters named total and percentage.

This function should return the amount you should tip given a total and the percentage you want to tip.

Hint
Calculating the tip value will look something like this: (total * percentage) / 100
'''
# Write your tip function here:
def tip(total, percentage):
  tip_final = ((total * percentage) / 100)
  return tip_final
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0

'''
3. Bond, James Bond
It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs. To accomplish this, we need to:

Define the function to accept two parameters, first_name and last_name
Concatenate the string ', ' on to the last_name
Concatenate the first_name on to the result of the previous step
Concatenate a space on to the result
Concatenate the last_name again to the result
Return the final string
'''
'''
Write a function named introduction() that has two parameters named first_name and last_name.

The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

Hint
In order to concatenate strings in python, we can use the + operator. For example, if we wanted to create the string 'Hello, how are you?' from multiple strings, we could do: 'Hello' + ', ' + 'how are you?'
'''
# Write your introduction function here:
def introduction(first_name, last_name):
  var_bond = (last_name + ", " + first_name + " " + last_name)
  return var_bond
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
#print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
'''
4. Dog Years
Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. This will require a few steps:

Define the function called dog_years to accept two parameters: name and age
Calculate the age of the dog in dog years
Concatenate the string with the dog’s name and age in dog years
Return the resulting string
'''
'''
Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"

Test this function with your name and your age!

Hint
Since the age in dog years age * 7 is a number, we need to convert it to a string when concatenating using str(). For example: 'The age is: '+ str(age * 7).
'''
# Write your dog_years function here:
def dog_years(name, age):
  dog_age = (age * 7)
  return name + ", you are " + str(dog_age) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

'''
5. All Operations
For the final code challenge, we are going to perform multiple mathematical operations on multiple inputs to the function. We will begin with adding the first two inputs, then we will subtract the third and fourth inputs. After that, we will multiply the first result and the second result. In the end, we will return the remainder of the previous result divided by the first input. We will also print each of the steps. The steps needed to complete this are:

Define the function to accept four inputs: a, b, c, and d
Print and store the result of a + b
Print and store the result of c - d
Print and store the first result times the second result
Return the previous result modulo a
'''
'''
Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.

First, print the sum of a and b.

Second, print c minus d.

Third, print the first number printed, multiplied by the second number printed.

Finally, return the third number printed modulo a.

Hint
To make this problem easier, you can store the result of each mathematical operation into a variable and use them as the results in step 4. For example: first_result = a + b. Also, remember that you can take the modulo of a number with %.
'''

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  alpha = (a+b)
  print(str(alpha))
  beta = (c-d)
  print(str(beta))
  gamma = (alpha * beta)
  print(str(gamma))
  delta = (gamma % a)
  print(str(delta))
  return delta
  
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0