'''
Challenges
We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your loop expertise.
'''

'''
1. Divisible By Ten
Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. These are the steps we need to complete this:

Define the function to accept one input parameter called nums
Initialize a counter to 0
Loop through every number in nums
Within the loop, if any of the numbers are divisible by 10, increment our counter
Return the final counter value
'''
'''
Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.

Hint
Create a counter that starts at 0. Inside the loop, whenever you find a number divisible by ten, add 1 to that counter.
x is divisible by ten if x % 10 == 0 is True.
'''
#Write your function here
def divisible_by_ten(nums):
  counter = 0
  for step in nums:
    if (step % 10 == 0):
      counter += 1
  return counter

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

'''
2. Greetings
You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name. This will require a few steps:

Define the function to accept a list of strings as a single parameter called names
Create a new list of strings
Loop through each name in names
Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
Afterwards, return the new list of strings
'''
'''
Create a function named add_greetings() which takes a list of strings named names as a parameter.
In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
Return the new list containing the greetings.
Hint
Use + to concatenate 'Hello, ' with every name in names. Don't forget to add the comma and the space to the greeting!
'''
#Write your function here
def add_greetings(names):
  greetings_list = []
  for name in names:
    name = "Hello, " + name
    greetings_list.append(name)
  return greetings_list


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

'''
3. Delete Starting Even Numbers
Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

Define our function to accept a single input parameter my_list which is a list of numbers
Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
Within the loop, if the first number in the list is even, then remove the first number of the list
Once we hit an odd number or we run out of numbers, return the modified list
'''
'''
Write a function called delete_starting_evens() that has a parameter named my_list.

The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.

For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!

Hint
Use a while loop to check two things. First, check if the list has at least one element, using len(my_list). Second, check to see if the first element is odd using mod (%). If both of those are True, slice off the first element of the list using my_list = my_list[1:].
'''
#Write your function here
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

'''
4. Odd Indices
This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

Define the function header to accept one input which will be our list of numbers
Create a new list which will hold our values to return
Iterate through every odd index until the end of the list
Within the loop, get the element at the current odd index and append it to our new list
Return the list of elements which we got from the odd indices.
'''
'''
Create a function named odd_indices() that has one parameter named my_list.

The function should create a new empty list and add every element from my_list that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

Hint
There are a few ways to do this. range(1, len(my_list), 2) will create a list of the indices you're interested in. So you could loop through that list like this:
for index in range(1, len(my_list), 2):
  my_new_list.append(my_list[index])

'''

#Write your function here
def odd_indices(my_list):
  my_list_new = []
  for index in range(1,len(my_list),2):
    my_list_new.append(my_list[index])
  return my_list_new


print(odd_indices([4, 3, 7, 10, 11, -2]))

'''
In our solution, we iterate through a range of values. The function range(1, len(my_list), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. This causes the loop to iterate through every odd number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd.
'''

'''
5. Exponents
In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:

Define the function to accept two lists of numbers, bases and powers
Create a new list that will contain our answers
Create a loop that iterates through every base in bases
Within that loop, create another loop that iterates through every power in power
Within that nested loop, append the result of the current base raised to the current power.
After all iterations of both loops are complete, return the list of answers
'''
'''
Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])

the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.
Hint
Use nested for loops. The outer for loop should loop through all of the bases and the inner for loop should loop through all of the powers.
Remember a ** b is a to the power of b
'''

#Write your function here
def exponents(bases,powers):
  answers = []
  for a in bases:
    for b in powers:
        a**b
        answers.append(a**b)
  return answers

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

'''
As you can see in this solution, we used two nested for loops so that, for every base, we iterate through every power. This allows us to raise each base to every single power in our list and append the answers to our new list. Finally, we return the list of answers.
'''