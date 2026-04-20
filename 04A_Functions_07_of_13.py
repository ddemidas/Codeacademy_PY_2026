# Write your code below: 
'''
task1
Our travel application users want to calculate the total expenses they may have to incur on a trip.

Write a function called calculate_expenses (replace <function> with the function name) that will have four parameters (in exact order):

plane_ticket_price
car_rental_rate
hotel_rate
trip_time
Each of these parameters will account for a different expense that our users will incur.

Note: Like before, we will see an error: SyntaxError: unexpected EOF while parsing, since there is no code in the body of the function. In the next step we will add statements to the function.
'''
'''
task2
Within the body of the function, let’s start to make some calculations for our expenses. First, let’s calculate the total price for a car rental.

Create new variable called car_rental_total that is the product of car_rental_rate and trip_time.
'''
'''
task3
Next, we want to apply the same logic but for our hotel_rate.

Create new variable called hotel_total that is the product of hotel_rate and trip_time.

We also have a coupon to give our users some cashback for their hotel visit so subtract 10 from that total in the same statement. Woohoo, coupons! 💵
'''
'''
task4
Lastly, create a new variable called trip_total that is the sum of car_rental_total, hotel_total, and plane_ticket_price.

Note: Do not delete return trip_total at the end of the function. This will output your new variable when the function is called.
'''
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  
  print("Total cost of your trip is " + str(trip_total))
  
  return trip_total
  
'''
task5
Call your function with the following argument values for the parameters listed:

plane_ticket_price : 200
car_rental_rate : 100
hotel_rate : 100
trip_time: 5
Be sure to call your function inside of print() so you can see the output.
'''
#calculate_expenses(200, 100, 100, 5)

plane_ticket_price = 200
car_rental_rate = 100
hotel_rate = 100
trip_time = 5
'''
#print("What is the ticket price? ")
plane_ticket_price = input("What is the ticket price?: ")
plane_ticket_price = int(plane_ticket_price)
#print("What is the rental rate? ")
car_rental_rate = input("What is the rental rate?: ")
car_rental_rate = int(car_rental_rate)
#print("What is the hotel rate? ")
hotel_rate = input("What is the hotel rate?: ")
hotel_rate = int(hotel_rate)
#print("What is the trip time? ")
trip_time = input("What is the trip time?: ")
trip_time = int(trip_time)
'''
calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time)


# Step 5: call your function