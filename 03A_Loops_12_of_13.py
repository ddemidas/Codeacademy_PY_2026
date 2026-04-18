heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
'''
task1
We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
'''
can_ride_coaster = []
can_ride_coaster = [participant for participant in heights if participant > 161]
print("Here is the list of who is allowed to ride the coaster: ")
print(can_ride_coaster)