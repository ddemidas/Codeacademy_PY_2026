votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
'''
task1
Mrs. Wilson’s class is voting for class president. She has saved each student’s vote into the list votes.
Use .count() to determine how many students voted for "Jake" and save the value to a variable called jake_votes.
'''
jake_votes = votes.count("Jake")
print("Jake has " + str(jake_votes) + " votes")