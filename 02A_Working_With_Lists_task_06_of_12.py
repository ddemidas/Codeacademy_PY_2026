long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
big_range = range(2, 3000, 100)
# Your code below: 
'''
task1
Calculate the length of long_list and save it to the variable long_list_len.
'''
long_list_len=len(long_list)
print("Length of a long list is: ")
print(long_list_len)
'''
task3
We have provided a completed range() function for the variable big_range.
Calculate its length using the function len() and save it to a variable called big_range_length.
Note: Range objects do not need to be converted to lists in order to determine their length
'''
small_range = range(2, 3000, 10)
small_range = list(small_range)
small_range_length = len(small_range)
'''
task4
Use print() to examine big_range_length.
'''
print(small_range_length)
'''
task5
Change the range() function that generates big_range so that it skips 100 instead of 10 steps between items.
How does this change big_range_length?
'''

#I don't know why but Codeacademy required me to remove line 32
#big_range = list(big_range)
big_range_length = len(big_range)
print(big_range_length)