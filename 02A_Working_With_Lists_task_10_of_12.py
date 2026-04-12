# Checkpoint 1 & 2
'''
Use .sort() to sort addresses.
'''
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
print(addresses)
addresses.sort()
print(addresses)
#Below assignment will be sensless because sort triggers the action, no assignement happens
#addresses_sorted=addresses.sort()
#print(addresses_sorted)

# Checkpoint 3
'''
Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.
'''
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
print(names)
#sort(names)
names.sort()
print(names)

# Checkpoint 4 & 5
'''
Use print to examine sorted_cities. Why is it not the sorted version of cities?
Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).
Print cities to see the result.
'''
#Because sort() is a trigger of action, it doesnt save any value
#the boolean parameter reverse as well as the value True or False are CASE SENSETIVE!
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
print(cities)
#sorted_cities = cities.sort()
#print(sorted_cities)
cities.sort(reverse = True)
print(cities)
