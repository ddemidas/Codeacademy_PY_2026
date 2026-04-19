##################################
#importing mean funtion from statistics module
from statistics import mean 
##################################

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

'''
task1
Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.
'''
total_price = 0
'''
task2
Loop through the prices list and add each price to the variable total_price.
'''
print("Adding all below prices according to the task2:")
for tmp_price in prices:
  total_price += tmp_price
  print(tmp_price)
print("Total price is: ")
print(total_price)

'''
task3
After your loop, create a variable called average_price that is the total_price divided by the number of prices.
You can get the number of prices by using the len() function.
'''
'''
task4
Print the value of average_price so the output looks like
'''
list_avg = mean(prices) 

print("Average Haircut Price:\n") 
print(list_avg) 
print("Average Haircut Price with precision upto 2 decimal value:\n")
print(round(list_avg,2))

'''
task5
That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
'''
'''
task6
Print new_prices.
'''
new_prices = [(tmp_price -5) for tmp_price in prices]
print("New prices are:\n")
print(new_prices)

list_avg_new = mean(new_prices)

print("New Average Haircut Price:\n")
print(list_avg_new)
print("New Average Haircut Price with precision upto 2 decimal value:\n")
print(round(list_avg_new,2))

'''
task7
Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.
Create a variable called total_revenue and set it to 0.
'''
total_revenue = 0
'''
task8
Use a for loop to create a variable i that goes from 0 to len(hairstyles)
Hint: You can use range() to do this!
'''
'''
task9
Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
'''
#print("DBG_DMDE" + str(list(range(len(hairstyles)))))
for i in list(range(len(hairstyles))):
  tmp_price = prices[i]
  #print(tmp_price)
for i in list(range(len(hairstyles))):
  tmp_revenue = last_week[i]
  #print(tmp_revenue)
for i in list(range(len(hairstyles))):
  total_revenue_tmp = prices[i]*last_week[i]
  #print(total_revenue_tmp)
  total_revenue += total_revenue_tmp
print("Total revenue for the last week is: \n")
'''
task10
After your loop, print the value of total_revenue, so the output looks like:
'''
print(total_revenue)
'''
task11
Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.
'''
weekdays_scheme = "Full"
match weekdays_scheme:
  case "Regular":
    number_of_week_days = 5
  case "Reinforced":
    number_of_week_days = 6
  case "Full":
    number_of_week_days = 7

print("This week we are working in the mode " + weekdays_scheme + " hence the number of weekdays is: " + str(number_of_week_days))

average_daily_revenue = total_revenue/number_of_week_days
print("Average daily revenue is: \n")
print(average_daily_revenue)
'''
task12
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
You can use range(len(new_prices)) in your list comprehension to make i go from 0 to the last index of new_prices.
'''
'''
task13
Print cuts_under_30.
'''
cuts_under_30 = []

#dbg print("New prices are: ")
#dbg print(new_prices)

for i in range(len(new_prices)):
  if (new_prices[i] < 30):
    cuts_under_30.append(hairstyles[i])
    print(new_prices[i])


print("Haircuts which are cheaper than 30 dollars according to the new prices: \n")
print(cuts_under_30)
