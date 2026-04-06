orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
print("orders: " + str(orders))
'''
task1
Jiho is updating a list of orders. He just received orders for "lilac" and "iris".

Create a list called new_orders that contains our new orders.
'''

# Create new orders here:
new_orders=["lilac", "iris"]
print("new_orders: "+str(new_orders))
'''
task2
Use + to create a new list called orders_combined that combines orders with new_orders.
'''
orders_combined =  orders+new_orders
print("orders_combined: "+str(orders_combined))

'''
Remove the # and whitespace in front of the list broken_prices. If you run this code, you’ll get an error:

TypeError: can only concatenate list (not "int") to list

Copy to Clipboard

Fix the command by inserting brackets ([ and ]) so that it will run without errors.
'''

broken_prices = [5, 3, 4, 5, 4] + [4]
print("broken_prices: "+str(broken_prices))