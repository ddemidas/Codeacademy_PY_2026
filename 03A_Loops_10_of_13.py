sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
'''
task1
We have provided the list sales_data that shows the number of scoops sold for different flavors of ice cream at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.
We want to sum up the total number of scoops sold across all three locations. Start by defining a variable scoops_sold and set it to zero.
'''
scoops_sold = 0
'''
task2
Loop through the sales_data list using the following guidelines:
For our temporary variable of the for loop, call it location.
print() out each location list.
'''
for location in sales_data:
  print(location)
'''
task3
Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.
By the end, you should have the sum of every number in the sales_data nested list.
'''
'''
task4
Print out the value of scoops_sold outside of the nested loop.
'''
for location in sales_data:
  for value in location:
    scoops_sold += value
print("scoops sold: " + str(scoops_sold))