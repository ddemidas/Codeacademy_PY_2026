#inspired by this page: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
#Importing the 'datetime' module
from datetime import datetime

#creating a date using year, month, day as arguments
birthday = datetime(1986, 2, 16, 2, 30)
print(birthday)
print(birthday.year)
print(birthday.month)

#Creating a date using datetime.now()
print(datetime.now())

print(datetime(2018, 1, 1) - datetime(2017, 1, 1))

age_marta = datetime.now() - datetime(2018, 3, 9)
print("Martas age is: " + str(age_marta))

#parsing a date using strptime
parsed_date = datetime.strptime('Mar 9, 2018', '%b %d, %Y')
print(parsed_date)
print(parsed_date.month)
print(parsed_date.day)
print(parsed_date.year)

