'''
Learn Python 3
Scrabble
In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.
'''

'''
Task1
We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.
Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
'''

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
print("======Project Build your Point Dictionary======")
print("Task1")
print("letter_to_points: ")
print(letter_to_points)

'''
Task2
Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
'''
print("Task2")
letter_to_points[" "]=0
print("letter_to_points: ")
print(letter_to_points)

'''
Task3, Task4, Task5, Task6, Task7, Task8
We want to create a function that will take in a word and return how many points that word is worth.
Define a function called score_word that takes in a parameter word.
Inside score_word, create a variable called point_total and set it to 0
After defining point_total, create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
You should get the point value from the letter_to_points dictionary. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.
After the for loop is finished, return point_total.
Let’s test this function! Create a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE".
'''
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

word = input("Please enter the word to be calculated for value: ")
#word = "Aquarius"
word = word.upper()

letter_to_points = {key:value for key, value in zip(letters, points)}
print("======Project Build your Point Dictionary======")
print("Task1")
print("letter_to_points: ")
print(letter_to_points)

print("Task2")
letter_to_points[" "]=0
print("letter_to_points: ")
print(letter_to_points)

print("Task3, Task4, Task5, Task6, Task7, Task8")
def f_score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return point_total

print("Let us test our funtion f_score_word for te word " + str(word)+":")
print(f_score_word(word))
