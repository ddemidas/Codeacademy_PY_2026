dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

'''
task1
You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.
Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.
Use the <temporary variable> name of dog_breed in your loop declaration
'''

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)

'''
task2
Inside your for loop, after you print each dog breed, check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"
'''

print("=======")
for dog_breed in dog_breeds_available_for_adoption:
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
  print("But the loop is continuing")
  print(dog_breed)

'''
task3
Add a break statement when your loop has found dog_breed_I_want so that the rest of the list does not need to be checked once we have found our breed.
'''
print("=======")
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    print("And this dog is: " + str(dog_breed))
    break
    
#print("Loop break condition has been reached")