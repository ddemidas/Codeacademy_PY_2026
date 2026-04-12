inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

'''
task1
Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.
Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.
First, how many items are in the warehouse?
Save the answer to a variable called inventory_len.
'''
inventory_len = len(inventory)
print(inventory_len)
'''
task2
Select the first element in inventory. Save it to a variable called first.
'''
first = inventory[0]
print("The first element of inventory is: ")
print(first)
'''
task3
Select the last element from inventory. Save it to a variable called last
'''
last = inventory[-1]
print("The last element of inventory is: ")
print(last)
'''
task4
Select items from the inventory starting at index 2 and up to, but not including, index 6.
Save your answer to a variable called inventory_2_6.
'''
inventory_2_6 = inventory[2:6]
print("Items of the list of inventory starting from position 2 till 6 but not including position 6: ")
print(inventory_2_6)
'''
task5
Select the first 3 items of inventory. Save it to a variable called first_3.
'''
first_3 = inventory[:3]
print("The first three items of inventory list: ")
print(first_3)
'''
task6
How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.
'''
twin_beds = inventory.count("twin bed")
print("The amount of Twin Beds in our inventory is: ")
print(twin_beds)
'''
task7
Remove the 5th element in the inventory. Save the value to a variable called removed_item.
'''
print("The list of invenroty before remove operation: ")
print(inventory)
removed_item = str(inventory[4])
print("--------")
print("DMDE_DBG: "+removed_item + " has to be removed because it is a fifth element in inventory list.")
print("--------")
inventory.remove(str(inventory[4]))
print("The list of invenroty after remove operation: ")
print(inventory)
print("Here is the list of what has been removed from our inventory so far: ")
print(removed_item)
'''
task8
There was a new item added to our inventory called "19th Century Bed Frame".
Use the .insert() method to place the new item as the 11th element in our inventory.
'''
inventory.insert(10,"19th Century Bed Frame")
print("Inventory list after adding an element described in task8: ")
print(inventory)
'''
task9
Sort inventory using the .sort() method or the sorted() function.
Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().
Print inventory to see the result.
'''
print("The list of inventory before sorting: ")
print(inventory)

inventory = sorted(inventory)

print("The list of inventory before sorting: ")
print(inventory)

