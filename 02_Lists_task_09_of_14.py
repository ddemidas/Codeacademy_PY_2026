# Your code below:
'''
task1
Define a list called garden_waitlist and set the value to contain our customers (in order): "Jiho", "Adam", "Sonny", and "Alisha".
'''
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
print("garden_waitlist: "+str(garden_waitlist))
'''
task2
"Adam" decided his fridge is too full at the moment and asked us to remove him from the waitlist and make space for one of our other townsfolk.

Replace "Adam" with our other interested customer "Calla" using the index method we used in the narrative.

Print garden_waitlist to see the change!
'''
garden_waitlist[1] = "Calla"
print("garden_waitlist: "+str(garden_waitlist))
#below print has been added because of an absurd task requiring to print the variable and not accepting above line
#Print garden_waitlist to see the change!
print(garden_waitlist)
'''
task3
Alisha realized she was already stocked with all the items we are selling. She asked us to replace her with her friend Alex who just ran out.

Replace Alisha with Alex using a negative index.

Print garden_waitlist again to see the change!
'''
garden_waitlist[-1]="Alex"
print("garden_waitlist: "+str(garden_waitlist))