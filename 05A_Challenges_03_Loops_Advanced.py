'''
Challenges
We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your loop expertise.
'''

'''
1. Larger Sum
We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

Define the function to accept two input parameters: lst1 and lst2
Create two variables to record the two sums
Loop through the first list and add up all of the numbers
Loop through the second list and add up all of the numbers
Compare the first and second sum and return the list with the greater sum
'''

'''
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

Hint
Create variables named sum1 and sum2 and set them to be 0. Loop through each list separately and add to the appropriate variable. After looping through each list, compare the two sums in an if statement and return the correct list.
'''

#Again, this is an example when Codeacademy engine is too strict.
#Task says "Compare the first and second sum and return the list with the greater sum"
#Task doesn't say what to do when the values are equal
#Below option is placed only because Codeacademy engine requires the code to look so:

#(01) Strict option required by Codeacademy:

#Write your function here
def larger_sum(lst1,lst2):
  sum1 = 0
  sum2 = 0
  for a in lst1:
    sum1 += a
  for b in lst2:
    sum2 += b
  if sum1 >= sum2:
    return lst1
  #elif sum1 == sum2:
  #  print("Summaries are equal, returning both lists: ")
  #  return lst1, lst2
  else:
    return lst2


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
#print(larger_sum([1, 9, 5], [5, 3, 7]))

#(02) My option which takes into consideration a separate case when summaries are equal:

#Write your function here
def larger_sum(lst1,lst2):
  sum1 = 0
  sum2 = 0
  for a in lst1:
    sum1 += a
  for b in lst2:
    sum2 += b
  if sum1 > sum2:
    return lst1
  elif sum1 == sum2:
    print("Summaries are equal, returning both lists: ")
    return lst1, lst2
  else:
    return lst2


#Uncomment the line below when your function is done
#print(larger_sum([1, 9, 5], [2, 3, 7]))
print(larger_sum([1, 9, 5], [5, 3, 7]))

'''
2. Over 9000
We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

Define the function to accept a list of numbers
Create a variable to keep track of our sum
Iterate through every element in our list of numbers
Within the loop, add the current number we are looking at to our sum
Still within the loop, check if the sum is greater than 9000. If it is, end the loop
Return the value of the sum when we ended our loop
'''
'''
Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

Hint
Create a variable named sum that begins at 0. Loop through all of the elements of lst and use a break when the sum is greater than 9000. Return sum after the loop.
'''
#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for i in lst:
    sum += i
    if (sum > 9000):
      print("sum is over 9000, end of algorhytm")
      break
  return sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

'''
3. Max Num
Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

Define the function to accept a list of numbers called nums
Set our default maximum value to be the first element in the list
Loop through every number in the list of numbers
Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
Return the maximum number
'''
'''
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums

Hint
Create a variable called maximum to track the max number, and have it start as the first element in the list. Loop through all of the numbers in the list, and if a number is ever greater than the current max number, the max number should be re-set to that number.
'''
#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

'''
4. Same Values
In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

Define our function to accept two lists of numbers
Create a new list to store our matching indices
Loop through each index to the end of either of our lists
Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
Return our list of indices
'''
'''
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

Hint
Loop through all of the indices of each list using for index in range(len(lst1)) and compare lst1[index] to lst2[index]. Append index to a new list if those two items are equal.
'''
#Write your function here
def same_values(lst1,lst2):
  list_return = []
  for index in range(len(lst1)):
    if (lst1[index] == lst2[index]):
      list_return.append(index)
  return list_return


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

'''
5. Reversed List
For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list. Here is what you need to do:

Define a function that has two input parameters for our lists
Loop through every index in one of the lists from beginning to end
Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
If the loop ended successfully, then we know the lists are reversed and we can return True.
'''
'''
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

Hint
Let's say the lists are of size 5. You want to compare lst1[0] with lst2[4], lst1[1] with lst2[3] and so on.
Loop through the numbers created by range(len(lst1)) using a variable named index

Compare lst1[index] to lst2[len(lst2) - 1 - index]. If those two items are not equal, return False. If you loop through the entire list and you never return False, that means that every item was equal, and you should return True.
'''
#Write your function here
def reversed_list(lst1,lst2):
  
  for index in range(len(lst1)):
    if (lst1[index] != lst2[len(lst2) -1 - index]):
      return False
  return True

#Uncomment the lines below when your function is done
#print(reversed_list([1, 2, 3, 4], [3, 2, 1]))
#print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))