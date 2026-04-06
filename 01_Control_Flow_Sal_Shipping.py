'''
task1
First things first, define a weight variable and set it equal to any number.
'''
'''
Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

Write a comment that says “Ground Shipping”.

Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.
'''
weight = 41.5
#weight = "Pawel"
cost=0.00
flat_charge_ground=20
#print(type(weight))
dbg_bool_type_checker_weight=(type(weight) == str)
#print("dbg_bool_type_checker_weight: "+str(dbg_bool_type_checker_weight))
#Ground shipping
if dbg_bool_type_checker_weight == True:
  print("Weight can not be a string, only numeric values please!")
elif float(weight) <= 2:
  cost=float(weight)*1.5+flat_charge_ground
  print("For Ground Shipping: cost of your delivery is: "+str(cost)+" USD")
elif float(weight) <=6:
  cost=float(weight)*3+flat_charge_ground
  print("For Ground Shipping: cost of your delivery is: "+str(cost)+" USD")
elif float(weight) <=10:
  cost=float(weight)*4+flat_charge_ground
  print("For Ground Shipping: cost of your delivery is: "+str(cost)+" USD")
elif float(weight) > 10:
  cost=float(weight)*4.75+flat_charge_ground
  print("For Ground Shipping: cost of your delivery is: "+str(cost)+" USD")
else:
  print ("Some other error has occurred")

'''
task3
A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:
8.4 lb×$4.00+$20.00=$53.60
Test that your ground shipping calculation gets the same value.
'''
#Ground Shipping Premium
'''
task4
We’ll also need to make sure we include the price of premium ground shipping in our code.

Create a variable for the cost of premium ground shipping.

Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.
'''
'''
task5
Using the variable you just created, print the cost of the Ground Shipping Premium.
'''
cost_ground_premium=0.00
flat_charge_ground_premium=125
cost_ground_premium=cost_ground_premium+flat_charge_ground_premium
if dbg_bool_type_checker_weight == True:
  print("Weight can not be a string, only numeric values please!")
elif dbg_bool_type_checker_weight == False:
  print("For Ground Shipping Premium cost is: "+str(cost_ground_premium))
else:
  print ("Some other error has occurred")

#Drone Shipping
'''
task6
Write a comment for this section of the code, “Drone Shipping”.

Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.
'''
cost_drone=0.00
flat_charge_drone=0
drone_multiplier=3

if dbg_bool_type_checker_weight == True:
  print("Weight can not be a string, only numeric values please!")
elif float(weight) <= 2:
  cost_drone=((float(weight)*1.5)*drone_multiplier)+flat_charge_drone
  print("For Drone Shipping: cost of your delivery is: "+str(cost_drone)+" USD")
elif float(weight) <=6:
  cost_drone=((float(weight)*3)*drone_multiplier)+flat_charge_drone
  print("For Drone Shipping: cost of your delivery is: "+str(cost_drone)+" USD")
elif float(weight) <=10:
  cost_drone=((float(weight)*4)*drone_multiplier)+flat_charge_drone
  print("For Drone Shipping: cost of your delivery is: "+str(cost_drone)+" USD")
elif float(weight) > 10:
  cost_drone=((float(weight)*4.75)*drone_multiplier)+flat_charge_drone
  print("For Drone Shipping: cost of your delivery is: "+str(cost_drone)+" USD")
else:
  print ("Some other error has occurred")

'''
task7
A package that weighs 1.5 pounds should cost $6.75 to ship by drone:
1.5 lb×$4.50+$0.00=$6.75
Test that your drone shipping calculation gets the same value.
'''
'''
task8
Great job! Now, test everything one more time!

What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
'''

