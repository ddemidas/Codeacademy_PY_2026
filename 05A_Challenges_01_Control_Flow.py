'''
====================Python Code Challenges: Control Flow====================
'''
num1 = 6
num2 = 3

# Write your if statement here
if (num1+num2) == 10:
  not_ten = False
else:
  not_ten = True

# Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten))

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = (food_bill + electricity_bill + internet_bill + rent)

# Check if the total is greater than the budget and store the result in over_budget
over_budget = (total > budget)

if over_budget == True:
  print("You are over the budget")
else:
  print("You are in the budget")

# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))

'''
====================Python Code Challenges: Control Flow (Advanced)====================
'''

'''
1. In Range
Create a function named in_range() that has three parameters named num, lower, and upper.
The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
'''
# Write your in_range function here:
def in_range(num, lower, upper):
  if (lower <= num <= upper):
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

'''
2. Same Name
We need to write a program that checks different names and determines if they are equal. We need to accept two strings and compare them. Here are the steps:
Define the function to accept two strings, your_name and my_name
Test if the two strings are equal
Return True if they are equal, otherwise return False

Create a function named same_name() that has two parameters named your_name and my_name.
If our names are identical, return True. Otherwise, return False.
'''
# Write your same_name function here:

def same_name(your_name, my_name):
  bool_checker = (your_name == my_name)
  return bool_checker

#Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

'''
3. Always False
There are some situations that you normally want to avoid when programming using conditional statements. One example is a contradiction. This occurs when your condition will always be false no matter what value you pass into it. Let’s create an example of a function that contains a contradiction. It will contain a few steps:

Define the function to accept a single parameter called num
Use a combination of <, > and and to create a contradiction in an if statement.
If the condition is true, return True, otherwise return False. The trick here is that because we’ve written a contradiction, the condition should never be true, so we should expect to always return False.
'''
'''
Create a function named always_false() that has one parameter named num.

Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

Hint
Try to think of an example of a condition which is always false. For example, a number cannot be greater than and less than itself at the same time.
'''
# Write your always_false function here:
def always_false(num):
  bool_checker = ((num < 0) and (num >= 0))
  return bool_checker
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
'''
4. Movie Review
We want to create a function that will help us rate movies. Our function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating. Here are the steps needed:

Define our function to accept a single number called rating
If the rating is equal to or less than 5, return "Avoid at all costs!"
If the rating was less than 9, return "This one was fun."
If neither of the if statement conditions were met, return "Outstanding!"
'''
'''
Create a function named movie_review() that has one parameter named rating.

If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

Hint
Use a series of if statements to test the different ranges. We can check each condition separately to determine which string to return.
'''

# Write your movie_review function here:
def movie_review(rating):
  if (0 < rating <= 5):
    return "Avoid at all costs!"
  elif (5 < rating <9):
    return "This one was fun."
  elif (9 <= rating <= 10):
    return"Outstanding!"
  else:
    return "Rating can be in range 0 - 10 only"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

print(movie_review(5))
print(movie_review(11))

'''
5. Max Number
For the final challenge, we are going to select which number from three input values is the greatest using conditional statements. To do this, we need to check the different combinations of values to see which number is greater than the other two. Here is what we need to do:

Define a function that has three input parameters, num1, num2, and num3
Test if num1 is greater than the other two numbers
If so, return num1
Test if num2 is greater than the other two numbers
If so, return num2
Test if num3 is greater than the other two numbers
If so, return num3
If there was a tie between the two largest numbers, then return "It's a tie!"
'''
'''
Create a function called max_num() that has three parameters named num1, num2, and num3.

The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

Hint
You can use if, elif, and else statements to accomplish this. For the first parameter, test if num1 is greater than num2 and that num1 is greater than num3. Repeat these tests for num2 and num3.
'''

# Write your max_num function here:
def max_num(num1, num2, num3):
  if ((num1 > num2) and (num1 > num3)) == True:
    #return (str(num1))
    return num1
  elif ((num2 > num1) and (num2 > num3)) == True:
    #return (str(num2))
    return num2
  elif ((num3 > num1) and (num3 > num2)) == True:
    #return (str(num3))
    return num3
  elif ((num1 == num2) or (num1 == num3)) or (num2 == num3) == True:
    return "It's a tie!"
  else:
    return "This function compares only numbers, please be careful!"
  

  

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
print(max_num(5, 2, 0))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
