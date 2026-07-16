'''
Task1
Suppose we have a dictionary of temperature sensors in the house and what temperatures they read. We’ve just added a sensor to the "pantry", and it reads 22 degrees.
Add this pair to the dictionary on line 1.
'''

'''
Task2
Remove the # in front of the definition of the dictionary num_cameras, which represents the number of cameras in each area around the house.
If you run this code, you’ll get an error:
'''

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

#For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
print(subtotal_to_total)


'''
Values can be of any 
type
Preview: Docs Loading link description
. We can use a string, a number, a list, or even another dictionary as the value associated 
with
Preview: Docs Loading link description
 a key!

For example:
'''

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

print(students_in_classes)

'''
The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in that class.
We can also mix and match key and value types. For example:
'''
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
print(person)

'''
Task1
Create a dictionary called translations that maps the following words in English to their definitions in Sindarin (the language of the elves):
'''

translations ={
  "mountain": "orod", 
  "bread": "bass", 
  "friend": "mellon", 
  "horse": "roch"
}
print(translations)

'''
We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these 
data types
Preview: Docs Loading link description
 as keys of the dictionary. If we 
try
Preview: Docs Loading link description
 to, we will get a TypeError.

For example:
'''
#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
powers = {2: [1, 2, 4, 8, 16],3: [1, 3, 9, 27, 81]}
print("powers are here: ")
print(powers)


#children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
print("children are here: ")
print(children)

'''
Creating Dictionaries
Add A Key
3 min
To add a single key: value pair to a dictionary, we can use the syntax:
dictionary[key] = value
'''

'''
For example, if we had our menu dictionary 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 the first exercise:
'''
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

print("menu before we do anything: ")
print(menu)

'''
And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:
'''
menu["cheesecake"] = 8

print("menu after adding new element: ")
print(menu)

animals_in_zoo = {}
print("animals_in_zoo before we add anyhing: ")
print(animals_in_zoo)
animals_in_zoo["zebras"] = 8
print("animals_in_zoo after adding one key-value pair: ")
print(animals_in_zoo)

print("animals_in_zoo before we add key-value pair with monkeys: ")
print(animals_in_zoo)

animals_in_zoo["monkeys"] = 12

print("animals_in_zoo after we add key-value pair with monkeys: ")
print(animals_in_zoo)

print("animals_in_zoo after we add key-value pair with dinosaurs: ")
print(animals_in_zoo)
animals_in_zoo["dinosaurs"] = 0
print("animals_in_zoo after we add key-value pair with dinosaurs: ")
print(animals_in_zoo)

'''
Creating Dictionaries
Add Multiple Keys
3 min
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the 
.update()
Preview: Docs Updates the dictionary with key-value pairs from another dictionary or iterable, overwriting existing keys if they exist.
 method.

Looking at our sensors object 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 a previous exercise:
'''
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

print("sensors before we update them: ")
print(sensors)

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

print("sensors after we update them: ")
print(sensors)


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

print("user_ids before we update them: ")
print(user_ids)

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print("user_ids after we update them: ")
print(user_ids)

'''
Creating Dictionaries
Overwrite Values
3 min
We know that we can add a key by using the following syntax:
'''
#menu["banana"] = 3

'''
This will create a key "banana" and set its value to 3. But what if we used a key that already has an entry in the menu dictionary?

In that case, our value assignment would overwrite the existing value attached to that key. We can overwrite the value of "oatmeal" like this:
'''
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("menu before overwriting the value for oatmeal")
print(menu)
menu["oatmeal"] = 5
print("menu after overwriting the value for oatmeal")
print(menu)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

print("oscar_winners before adding Viola Davis: ")
print(oscar_winners)
oscar_winners["Supporting Actress"] = "Viola Davis"
print("oscar_winners after adding Viola Davis: ")
print(oscar_winners)

print("oscar_winners before amending Best Picture: ")
print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"
print("oscar_winners before amending Best Picture: ")
print(oscar_winners)

'''
Creating Dictionaries
Dict Comprehensions
8 min
Let’s say we have two 
lists
Preview: Docs Loading link description
 that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:
'''


names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

print("List of names: ")
print(names)
print("List of heights: ")
print(heights)

students = {key:value for key, value in zip(names, heights)}

print("Combined list of student names and heights: ")
print(students)

'''
You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.
'''

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print("The resulting list will look like: ")
print(drinks_to_caffeine)


'''
Expected library to be: {‘The Best Songs’: {‘Like a Rolling Stone’: 78, ‘Satisfaction’: 29, ‘Imagine’: 44, “What’s Going On”: 21, ‘Respect’: 94, ‘Good Vibrations’: 5, ‘Purple Haze’: 1, ‘Sunday Feelings’: 0}, ‘Sunday Feelings’: {}}
'''

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

zipper = zip(songs, playcounts)

plays = {key:value for key, value in zipper}

print("plays before update: ")
print(plays)

plays.update({"Purple Haze": 1})

print("plays after update: ")
print(plays)

plays.update({"Respect": 94})

print("plays after update: ")
print(plays)

library = {}
print("Dictionary library has been created and it is empty: ")
print(library)

library["The Best Songs"] = plays
print(library)

library["Sunday Feelings"] = {}
print(library)

