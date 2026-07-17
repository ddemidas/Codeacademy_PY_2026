'''
Using Dictionaries
Get A Key
3 min
Once you have a dictionary, you can access the values in it by providing the key. For example, let’s imagine we have a dictionary that maps buildings to their heights, in meters:
'''

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

print(building_heights["Burj Khalifa"]) # Prints 828
print(building_heights["Ping An"]) # Prints 599

'''
Task1
We have provided a dictionary that maps the elements of astrology to the zodiac signs. Print out the list of zodiac signs associated with the "earth" element.
'''

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print("earth signs: ")
print(zodiac_elements["earth"])
print("water signs: ")
print(zodiac_elements["water"])
print("air signs: ")
print(zodiac_elements["air"])
print("fire signs: ")
print(zodiac_elements["fire"])

'''
Using Dictionaries
Get an Invalid Key
6 min
Let’s say we have our dictionary of building heights 
from
Preview content is loading
 the last exercise:
'''

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

'''
What if we wanted to know the height of the Landmark 81 in Ho Chi Minh City? We could try:
'''

#print(building_heights["Landmark 81"])

'''
But "Landmark 81" does not exist as a key in the building_heights dictionary! So this will throw a KeyError:
KeyError: 'Landmark 81'
'''

'''
One way to avoid this error is to first check if the key exists in the dictionary:
'''

key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], "energy":"Not a Zodiac element"}


key_to_check = "energy"

if key_to_check in zodiac_elements:
  print(zodiac_elements["energy"])
else:
  print("This key is not in our dictionary")

print(zodiac_elements)

'''
Using Dictionaries
Safely Get a Key
6 min
We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError. This solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our dictionary!

Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will 
return
Preview: Docs Loading link description
 None by default:
'''

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")

'''
You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:
'''

print(building_heights.get('Shanghai Tower', 0)) # Prints 632
print(building_heights.get('Mt Olympus', 0)) # Prints 0
print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'


user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print("tc_id: ")
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print("stack_id: ")
print(stack_id)

'''
Using Dictionaries
Delete a Key
12 min
Sometimes we want to get a key and remove it 
from
Preview: Docs Loading link description
 the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:
'''

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))
# Prints "Gift Basket"
print(raffle)
# Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
# Prints "No Prize"
print(raffle)
# Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
# Prints "Concert Tickets"
print(raffle)
# Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

'''
Task1
You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.
'''

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print("health_points: "+ str(health_points))

print("available_items:")
print(available_items)

'''
Using Dictionaries
Get All Keys
7 min
Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:
'''

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

'''
We want to get a roster of the students in the class, without including their grades. We can do this 
with
Preview: Docs Loading link description
 the built-in 
list()
Preview: Docs Loading link description
 function:
'''
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

'''
Dictionaries also have a 
.keys()
Preview: Docs Returns a list of keys for a dictionary.
 method that returns a dict_keys object. A dict_keys object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything. The dict_keys object returned by .keys() is a set of the keys in the dictionary. You cannot add or remove elements 
from
Preview content is loading
 a dict_keys object, but it can be used in the place of a list for iteration:
'''

'''
Dictionaries also have a 
.keys()
Preview: Docs Returns a list of keys for a dictionary.
 method that returns a dict_keys object. A dict_keys object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything. The dict_keys object returned by .keys() is a set of the keys in the dictionary. You cannot add or remove elements 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 a dict_keys object, but it can be used in the place of a list for iteration:
'''
for student in test_scores.keys():
 print(student)
'''
Grace
Jeffrey
Sylvia
Pedro
Martin
Dina
'''

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print("users: ")
print(users)
print("num_exercises: ")
print(num_exercises)

'''
Using Dictionaries
Get All Values
5 min
Dictionaries
Preview: Docs A dictionary is a data set of key-value pairs.
 have a 
.values()
Preview: Docs Loading link description
 method that returns a dict_values object (just like a dict_keys object but for values!) 
with
Preview: Docs Simplifies resource management by automatically handling setup and teardown actions using context managers.
 all of the values in the dictionary. It can be used in the place of a list for iteration:
'''

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
 print(score_list)

'''
will yield:

[80, 72, 90]
[88, 68, 81]
[80, 82, 84]
[98, 96, 95]
[78, 80, 78]
[64, 60, 75]

'''

'''
There is no built-in function to get all of the values as a list, but if you really want to, you can use:
'''
'''
list(test_scores.values())

However, for most purposes, the dict_values object will act the way you want a list to act.
'''

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for points in num_exercises.values():
  total_exercises += points

print("total_exercises: ")
print(total_exercises)

'''
Get All Items
6 min
You can get both the keys and the values 
with
Preview: Docs Loading link description
 the 
.items()
Preview: Docs Returns a list of tuples for each key-value pair in a dictionary.
 method. Like 
.keys()
Preview: Docs Returns a list of keys for a dictionary.
 and 
.values()
Preview: Docs Returns a view of values for a dictionary.
, it returns a dict_list object. Each element of the dict_list returned by .items() is a tuple consisting of:

(key, value)

so to iterate through, you can use this syntax:
'''

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")

'''
which would 
yield
Preview: Docs Turns a function into a generator, producing values one at a time while retaining state between calls.
 this output:

Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.
'''

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + str(occupation) + "s.")


'''
Using Dictionaries
Review
10 min
In this lesson, you’ve learned how to go through 
dictionaries
Preview: Docs Loading link description
 and access keys and values in different ways. Specifically, you have seen how to:

Use a key to get a value 
from
Preview: Docs Loading link description
 a dictionary
Check for existence of keys
Remove a key: value pair from a dictionary
Iterate through keys and values in dictionaries
'''

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

print("tarot: ")
print(tarot)

print("spread: ")
print(spread)

for time, prediction in spread.items():
  print("Your " + str(time) + " is " + "the " + str(prediction) + " card.")