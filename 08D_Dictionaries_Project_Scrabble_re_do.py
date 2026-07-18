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
Task2
Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
'''

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key.upper():value for key, value in zip(letters, points)}
letter_to_points[" "]=0

print("======Project Build your Point Dictionary======")
print("Task1, Task2")
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

def f_play_word(player, word):
    word = word.upper()
    player = player.title()
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]
    return player, word

def f_play_round():
  player = input("Enter player's name: ")
  word = input(f"Enter {player}'s word to calculate their points score: ")
  f_play_word(player, word)



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

'''
Task9
Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:
'''

print("Task9")
player_to_words = {}

player_to_words.update({"player1":["BLUE","TENNIS","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con": ["ERASER","BELLY","HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]})

print("player_to_words: ")
print(player_to_words)

'''
Task10, Task11, 
Create an empty dictionary called player_to_points.
Iterate through the items in player_to_words. Call each player player and each list of words words.
Within your loop, create a variable called player_points and set it to 0.
Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input.
After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.
player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!
If you’ve calculated correctly, wordNerd should be winning by 1 point.

'''

print("Task10, Task11, Task12, Task13, Task14")
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  
  for word in words:
    player_points += f_score_word(word)
  #print("This player " + str(player) + " has " +str(player_points) + " points")
  #print(player)
  player_to_points.update({player:player_points})
print("player_to_points: ")
print(player_to_points)

'''
Task15
If you want extended practice, try to implement some of these ideas with the Python you’ve learned:
- play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
- update_point_totals() — turn your nested loops into a function that you can call any time a word is played
- make your letter_to_points dictionary able to handle lowercase inputs as well
'''
f_play_round()

print("player_to_words: ")
print(player_to_words)