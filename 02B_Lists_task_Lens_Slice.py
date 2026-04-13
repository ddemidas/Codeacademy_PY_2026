# Your code below:
'''
task1
To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
"pepperoni"
"pineapple"
"cheese"
"sausage"
"olives"
"anchovies"
"mushrooms"
'''
toppings = [
"pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"  
  ]

print("Pizzas which we can offer: ")
print(toppings)
print("----------")

'''
task2
To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
2
6
1
3
2
7
2
'''
prices = [
  2,
6,
1,
3,
2,
7,
2
]
print("Prices for pizzas are the following: ")
print(prices)
print("----------")

'''
task3
Your boss wants you to do some research on $2 slices.
Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
'''
num_two_dollar_slices = prices.count(2)
print("Number of 2 dollar slices is: ")
print(num_two_dollar_slices)
print("----------")

'''
task4
Find the length of the toppings list and store it in a variable called num_pizzas.
'''
num_pizzas = len(toppings)
print("Amount of pizzas kinds is: ")
print(num_pizzas)
print("----------")

'''
task5
Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
'''
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
print("----------")

'''
task6
Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

Each sublist in pizza_and_prices should have one pizza topping and an associated price.

Price	Topping
2	"pepperoni"
6	"pineapple"
1	"cheese"
3	"sausage"
2	"olives"
7	"anchovies"
2	"mushrooms"

For this new list make sure the prices come before the topping name like so:

[price, topping_name]

Copy to Clipboard

Note: You don’t need to use your original toppings and prices lists in this exercise. Create a new two-dimensional list from scratch.
'''

pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]
print("Here is pizzas with prices: ")
print(pizza_and_prices)
print("----------")
'''
task8
Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
'''

pizza_and_prices_bckp = pizza_and_prices
pizza_and_prices.sort()
print("Sorted pizzas by prices: ")
print(pizza_and_prices)
print("----------")

'''
task9
Store the first element of pizza_and_prices in a variable called cheapest_pizza.
'''
#print("dbg: ")
#print(pizza_and_prices [1])
#print("====")
cheapest_pizza = pizza_and_prices[0]
print("The cheapest pizza is: ")
print(cheapest_pizza)
print("----------")
'''
task10
A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
'''
priciest_pizza = pizza_and_prices[-1]
print("The priciest pizza is: ")
print(priciest_pizza)
print("----------")

'''
task11
It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
'''
print("Pizzas before removing the priciest one: ")
print(pizza_and_prices)
pizza_and_prices.pop()
print("Pizzas after removing the priciest one: ")
print(pizza_and_prices)
print("----------")
'''
task12
Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:

[2.5, "peppers"]

Copy to Clipboard

Add the new peppers pizza topping to our list pizza_and_prices.

Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!
'''
print("Pizzas before adding the peppers one: ")
print(pizza_and_prices)
pizza_and_prices.insert(-2, [2.5, "peppers"])
print("Pizzas after removing the peppers one: ")
print(pizza_and_prices)
print("----------")
'''
task13

Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
'''
three_cheapest = pizza_and_prices[0:3]
print("The three cheapest pizzas are: ")
print(three_cheapest)
print("----------")
