'''
====================Python Code Challenges: Lists====================
'''

'''
1. Append Size
For the first code challenge, we are going to calculate the length of an input list and append it to the end of the original list. For example, if we have the input list [23, 42, 108], which is of length 3, the output list should be [23, 42, 108, 3]. Similarly, the output for the input list [1, 23] should be [1, 23, 2].

Here is what you need to do:

Define a function append_size() that accepts a list as its input.
Get the length of the input list.
Append the length of the list to the end of the original list.
Return the modified list.
'''
'''
Create a function called append_size() that has one parameter named my_list.

The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.

For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

Hint
Remember that we can get the length of a list using len(). We can also append to the end of a list using append().
'''

# Write your function here
def append_size(my_list):
  member_to_append = int(len(my_list))
  my_list.append(member_to_append)
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

'''
2. Append Sum
For the next challenge, let’s create a function that calculates the sum of the last two elements of an input list and appends it to the end of the original list. After doing so, it repeats this process two more times and returns the resulting list.

For example, for the input list [1, 1, 2], the output list should be [1, 1, 2, 3, 5, 8]. Similarly, the output for the input list [1, 23] should be [1, 23, 24, 47, 71].

To complete the challenge, you need to implement the following:

Define the function append_sum() to accept a list as its input argument.
Add the last and second-to-last elements of the input list.
Append the calculated sum to the end of the input list.
Repeat the previous two steps two more times for the modified list.
Return the modified list.
'''
'''
Write a function named append_sum() that has one parameter — a list named named my_list.

The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.

For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

Hint
In order to get the last element of a list we can use my_list[-1]. The negative index starts from the end of the list and moves towards the front. Because of this, to get the second to last number we can use my_list[-2]. Additionally, to append items to a list we can use the append() function.
'''
#simpler solution
# Write your function here
def append_sum(my_list):
  my_list_tail_01 = int(my_list[-1])+int(my_list[-2])
  my_list.append(my_list_tail_01)
  my_list_tail_02 = int(my_list[-1])+int(my_list[-2])
  my_list.append(my_list_tail_02)
  my_list_tail_03 = int(my_list[-1])+int(my_list[-2])
  my_list.append(my_list_tail_03)
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
#more complicated solution with the loop

# Write your function here
def append_sum(my_list):
  print("my list is: " + str(my_list))
  for i in range(3):
    my_list.append(int(my_list[-1]) + int(my_list[-2]))
  return my_list
# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

'''
3. Larger List
Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt.

In our code, we can represent the id of the items using numbers and conveyor belts using lists. For instance, if we have two lists, [23, 12, 21] and [1, 23], representing the id of the items at two conveyor belts, the output will be 21. Similarly, for input lists [1, 7, 2, 3, 17] and [1, 23, 24, 47, 71, 83], the output will be 83. For input lists [23, 12, 21] and [1, 23, 25], the output will be 21 as both lists are of the same length.

Here are the steps you need to complete this code challenge:

Define a function that accepts two parameters for our two lists of numbers.
Check if the length of the first list is greater than or equal to the length of the second list.
If true, then return the last element from the first list. Otherwise, return the last element from the second list.
'''
'''
Write a function named larger_list() that has two parameters named my_list1 and my_list2.

The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.

Hint
Remember that we can use len(my_list1) to get the length of a list called my_list1. Also, to get the last element of my_list1 we can use my_list1[-1].
'''
# Write your function here
def larger_list(my_list1, my_list2):
  bool_checker1 = (len(my_list1) > len(my_list2))
  bool_checker2 = (len(my_list1) == len(my_list2))
  if bool_checker2 == True:
    return my_list1[-1]
  elif bool_checker1 == True:
    return my_list1[-1]
  elif bool_checker1 == False:
    return my_list2[-1]
  else:
    return "Are you sure your both list are not empty?"

# Uncomment the line below when your function is done
#option1
print(larger_list([4, 10, 2, 75], [-10, 2, 5, 10]))
#option2
print(larger_list([4, 10, 2, 75], [-10, 2, 5, 10, 100]))

#Code after refinement, we can manage with one boolean checker because >= combine two conditions for printing the last elemenr of my_list1
# Write your function here
def larger_list(my_list1, my_list2):
  bool_checker1 = (len(my_list1) >= len(my_list2))
  if bool_checker1 == True:
    return my_list1[-1]
  elif bool_checker1 == False:
    return my_list2[-1]
  else:
    return "Are you sure your both list are not empty?"

# Uncomment the line below when your function is done
#option1
print(larger_list([4, 10, 2, 75], [-10, 2, 5, 10]))
#option2
print(larger_list([4, 10, 2, 75], [-10, 2, 5, 10, 100]))

'''
4. More Than N
Our factory produces a variety of different flavored snacks. The different types of snacks are represented by their id and are kept on a conveyor belt. We want to check if we have enough items of a certain snack in our inventory. For this, we need to write a Python function that does the following.

The function should accept a list of numbers representing the ids of snack on the conveyor belt as its first input, the id of snack we are looking for as its second input, and the desired number of that type of snack on the conveyor belt as its third input.
The function should return True if the snack we are searching for appears more times in the list than the desired number given in the third parameter. Otherwise, it should return False.
Following are the steps we need to implement the above scenario:

Define the function to accept three parameters: a list of numbers, a number to look for, and a number for the number of instances.
Count the number of occurrences of item i.e. the second parameter in my_list i.e. the first parameter.
If the number of occurrences is greater than n i.e. the third parameter, return True. Otherwise, return False.
'''
'''
Create a function named more_than_n() that has three parameters named my_list, item, and n.

The function should return True if item appears in the list more than n times. The function should return False otherwise.

Hint
In order to easily count the number of occurrences of item in my_list we can use the count() function.
'''

# Write your function here
def more_than_n(my_list, item, n):
  digital_checker = my_list.count(item)
  boolean_checker = (digital_checker > n)
  if (boolean_checker == True):
    return boolean_checker
  else:
    return boolean_checker
  

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

'''
5. Combine Sort
Finally, let’s create a function that combines two different lists together and then sorts them. To do this, we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

Define the function to accept two parameters, one for each list.
Combine the two lists using the + operator.
Sort the resultant list after concatenation.
Return the sorted list.
'''
'''
Write a function named combine_sort() that has two parameters named my_list1 and my_list2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.

Hint
We can combine lists using the + operator. In order to sort a list we can use the sorted() function.
'''

# Write your function here
def combine_sort(my_list1, my_list2):
  print("Initial lists below: ")
  print(my_list1)
  print(my_list2)
  list_combined = my_list1 + my_list2
  print("Combined list below: ")
  print(list_combined)
  list_sorted = sorted(list_combined)
  return list_sorted


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))