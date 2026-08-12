"""
1/14
Introduction to Classes
Types
5 min
Python equips us 
with
Preview: Docs Loading link description
 many different ways to store data. A float is a different kind of number 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 an int, and we store different data in a list than we do in a dict. These are known as different types. We can check the type of a Python variable using the 
type()
Preview: Docs Loading link description
 function.
"""
a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints <class 'str'>

print(type(an_int))
# prints <class 'int'>

#Task1
#Call type() on the integer 5 and print the result.

#Task2
#Define a dictionary my_dict using curly braces {}.
#The dictionary can be empty, such as:

#Task3
#Print out the type() of my_dict.

#Task4
#Define a list called my_list.

#Task5
#Print out the type() of my_list.

print(type(an_int))
# prints <class 'int'>

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

"""
2/14
Introduction to Classes
Class
2 min
A 
class
Preview: Docs Loading link description
 is a template for a data type. It describes the kinds of information that the class will hold and how a programmer will interact 
with
Preview: Docs Loading link description
 that data. We define a class using the 
class
Preview: Docs Loading link description
 keyword. PEP 8 Style Guide for Python Code recommends capitalizing the names of classes to make them easier to identify.
"""
class CoolClass:
  pass
"""
In the example, we created a class and named it CoolClass. We used the 
pass
Preview: Docs Loading link description
 keyword in Python to indicate that the body of the class was intentionally left blank, so we don’t cause an IndentationError. We’ll learn about all the things we can put in the body of a class in the next few exercises.
"""
#Task1
#Define an empty class called Facade. We will add to it soon.
class Facade:
  pass
"""
3/14
Introduction to Classes
Instantiation
2 min
A class doesn’t accomplish anything simply by being defined. A class must be instantiated. In other words, we must create an instance of the class in order to breathe life into the schematic.
Instantiating a class is similar to calling a function. We would be able to create an instance of our defined CoolClass as follows:
"""
cool_instance = CoolClass()
"""
In the example, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable cool_instance for safekeeping so we can access our instance of CoolClass at a later time.
"""
#Task1
#In script.py, we see our Facade class from the last exercise. Make a Facade instance and save it to the variable facade_1.
class Facade:
  pass
facade_1 = Facade()
"""
4/14
Introduction to Classes
Object-Oriented Programming
4 min
A class instance is also called an object. The pattern of defining 
classes
Preview: Docs Loading link description
 and creating objects to represent the responsibilities of a program is known as 
Object-Oriented Programming
Preview: Docs Loading link description
 or OOP.

Instantiation takes a class and turns it into an object — the 
type()
Preview: Docs Loading link description
 function does the opposite of that. When called 
with
Preview: Docs Loading link description
 an object, it returns the class that the object is an instance of.
"""
print(type(cool_instance))
# prints <class '__main__.CoolClass'>
"""
We then print out the type() of cool_instance, and it shows us that this object is of type __main__.CoolClass.

In Python, __main__ means “this current file that we’re running”, and so we can read the output 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 type() to mean “the class CoolClass that was defined here, in the script we’re currently running.”
"""
#Task1
#In script.py, we see facade_1 from the last exercise. Try calling type() on facade_1 and saving it to the variable facade_1_type.
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

"""
5/14
Introduction to Classes
Class Variables
5 min
When we want the same data to be available to every instance of a class, we use a class variable. A class variable is a variable that’s the same for every instance of the class.

We can define a class variable by including it in the indented part of our class definition, and we can access all of an object’s class 
variables
Preview: Docs Loading link description
 
with
Preview: Docs Loading link description
 object.variable syntax.
"""
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints Rockstar
"""
In the example, we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string "Rockstar".
If we defined another musician, like guitarist = Musician(), they would have the same .title attribute.
Note: Class variables are often referenced with a leading period, like .title in the example. This is done to quickly show that the variable belongs to a class and must be accessed with dot notation, like drummer.title.
"""
#Task1
#You are digitizing grades for Jan van Eyck High School and Conservatory. At Jan van High, as the students call it, 65 is the minimum passing grade.
#Create a Grade class with a class attribute minimum_passing equal to 65.
class Grade:
  minimum_passing = 65
"""
6/14
Introduction to Classes
Methods
8 min
Methods are 
functions
Preview: Docs Loading link description
 that are defined as part of a class. The first parameter in a method is always the object that is calling the method. Convention recommends that we name this first parameter self. Methods always have at least one parameter.

We define methods similarly to functions, 
except
Preview: Docs Catches and handles exceptions raised in the try block.
 that they are indented to be part of the class.
"""
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints Dogs experience 7 years for every 1 human year.

"""
We created a Dog class 
with
Preview: Docs Loading link description
 a .time_explanation() method that takes one parameter, self, which refers to the object calling the method. We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.

Notice we didn’t 
pass
Preview: Docs Acts as a placeholder in Python code, allowing empty code blocks to run without causing errors.
 any arguments when we called .time_explanation(), but we were able to refer to self in the method body. When we call a method, it automatically passes the object calling the method as the first argument.
"""
"""
#Task1
At Jan van High, the students are constantly calling the school rules into question. Create a Rules class so that we can explain the rules.
In order for your code to run, you have to have something in your class — you can’t have a defined class with no body like the following:
class exampleClass:
Copy to Clipboard
For now, make the body of your class pass. This will allow your code to run without error.
"""
"""
Task2
Give Rules a method washing_brushes that returns the string "Point bristles towards the basin while washing your brushes."
Since we’ve now given this class a method, we can remove the pass that we added in the previous step.
"""
class Rules:
  motto = "Point bristles towards the basin while washing your brushes."

  def washing_brushes (self):
    return self.motto