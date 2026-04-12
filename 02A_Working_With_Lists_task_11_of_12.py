games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
'''
task1
Use sorted() to order games and create a new list called games_sorted.
'''
'''
task2
Print both games and games_sorted. How are they different?
'''
print("Original list of games looks like below: ")
print(games)
games_sorted = sorted(games)
print("Sorted list of games looks like below: ")
print(games_sorted)
#games_sorted.sort(reverse = True)
#print(games_sorted)
#These below two lines are needed only because Codeacademy doesn't accept the solution without having two variables printed out like below:
print(games)
print(games_sorted)