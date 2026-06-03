'''
1. Tenth Power
Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:

Set up the function header for tenth_power which accepts one parameter
Take the tenth power of the input value
Return the result
'''
'''
Write a function named tenth_power() that has one parameter named num.

The function should return num raised to the 10th power.

Hint
Remember to use def when defining the function. To take the power of a value, you can use the power operator **. For example, two to the power of five would look like: 2 ** 5.
'''
# Write your tenth_power function here:
def tenth_power(num):
  num_pwr_10 = num ** 10
  return num_pwr_10

# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
'''
2. Square Root
Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. We need to:

Set up the function header for square_root which accepts one parameter
Take the square root of the input value
Return the result
'''
'''
Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num.

Hint
Remember to use def when defining the function. To take the square root of a value, you can use the power operator **. The square root of a number is the same as taking the ½ power of the number. For example, the square root of 6 would look like: 6 ** 0.5.
'''
# Write your square_root function here:
def square_root(num):
  num_root = num ** 0.5
  return num_root
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10
'''
3. Win Percentage
Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

Define the function header with two parameters, wins and losses
Calculate the total number of games using the number of wins and losses
Get the ratio of winning using the number of wins out of the total number of games.
Convert the ratio to a percentage
Return the percentage
'''
'''
Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers.

Hint
In order to calculate the ratio of wins out of total games we can use wins / (wins + losses) where wins + losses is equal to the total number of games. To convert that value to a percentage, multiply it by 100.
Code
1234567
'''
# Write your win_percentage function here:
def win_percentage(wins, losses):
  win_ratio = (wins/(wins+losses))*(100)
  return win_ratio
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
'''
4. Average
Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:

Define the function with two input parameters, num1 and num2
Calculate the sum of the two numbers
Divide the sum by the number of inputs to the function
Return the answer
'''
'''
Write a function named average() that has two parameters named num1 and num2.

The function should return the average of these two numbers.

Hint
To calculate the average of two numbers we add the first and second number, then divide the result by 2: (first + second) / 2
'''
# Write your average function here:
def average(num1,num2):
  avg = (num1 + num2)/2
  return avg

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
'''
5. Remainder
For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this we will need to:

Define the function to accept two parameters
Multiply the first input value by 2
Divide the second input value by 2
Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
Return the answer
'''
'''
Write a function named remainder() that has two parameters named num1 and num2.

The function should return the remainder of twice num1 divided by half of num2.

Hint
In order to calculate the remainder of two numbers, we can use the modulus operator %. For example, the remainder of 5 divided by 2 is equal to 1 and we can get this result using 5 % 2.
'''
# Write your remainder function here:
def remainder(num1, num2):
  rem = ((2 * num1) % (num2/2))
  return rem

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0