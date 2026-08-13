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

"""
7/14
Methods can also take more parameters than just self:
"""
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints 8.045
"""
In the example, we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. Notice again that even though how_many_kms takes two parameters in its definition, we only 
pass
Preview: Docs Acts as a placeholder in Python code, allowing empty code blocks to run without causing errors.
 miles, because self is implicitly passed (and refers to the object converter).
"""
"""
#Task1, #Task2, #Task3, #Task4
It’s March 14th (known in some places as Pi Day) at Jan van High, and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.
Create a Circle class with a class variable pi. Set pi to the approximation 3.14.

Give Circle an area method that takes two parameters: self and radius.

Return the area as given by this formula:
area = pi * radius ** 2

Create an instance of Circle. Save it into the variable circle.

You go to measure several circles you happen to find around.

A medium pizza that is 12 inches across
Your teaching table, which is 36 inches across
The Round Room auditorium, which is 11460 inches across
You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area.

Remember that the radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.
"""
class Circle():
  pi = 3.14
  def area(self, radius):
    area = (self.pi)*(radius)**2
    return area

circle = Circle()
print(type(circle))

def radius(across):
  radius = ((across)/2)
  return radius

#print(radius(14))

across_pizza = 12
across_teaching_table = 36
across_auditorium = 11460

pizza_area = circle.area(radius(across_pizza))
print("pizza_area: ")
print(pizza_area)

teaching_table_area = circle.area(radius(across_teaching_table))
print("teaching_table_area: ")
print(teaching_table_area)

round_room_area = circle.area(radius(across_auditorium))
print("round_room_area: ")
print(round_room_area)

"""
8/14

Introduction to Classes
Constructors
12 min
There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called magic, because they behave differently 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 regular methods. Another popular term is 
dunder methods
Preview: Docs Loading link description
, so named because they have two underscores (double underscore abbreviated to “dunder”) on either side of them.

The first dunder method we’re going to use is the 
__init__()
Preview: Docs Loading link description
 method (note the two underscores before and after the word “init”). This method is used to initialize a newly created object. It is called every time the class is instantiated.

Methods that are used to prepare an object being instantiated are called constructors. The word “constructor” is used to describe similar features in other object-oriented programming languages, but programmers who refer to a constructor in Python are usually talking about the __init__() method.
"""
class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints HELLO?!

shout2 = Shouter()
# prints HELLO?!
"""
In the preceding example, we created a class called Shouter, and every time we create an instance of Shouter, the program prints out a shout. Don’t worry, this doesn’t hurt the computer at all.

Pay careful attention to the instantiation syntax we use. Shouter() looks a lot like a function call, doesn’t it? If it’s a function, can we 
pass
Preview: Docs Loading link description
 arguments to it? We absolutely can, and those arguments will be received by the __init__() method.
"""
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints SHOUT

shout2 = Shouter("shout")
# prints SHOUT

shout3 = Shouter("let it all out")
# prints LET IT ALL OUT
"""
In the preceding example, we’ve updated our Shouter class to take the additional parameter phrase. When we created each of our objects, we passed an argument to the constructor. The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.
"""
"""
#Task1
Add a constructor to our Circle class.
Since we seem more frequently to know the diameter of a circle, it should take the parameter diameter.
It doesn’t need to do anything yet; just write pass in the body of the constructor.
"""
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    pass
"""
#Task2
Now have the constructor print out the message New circle with diameter: {diameter} when a new circle is created.
Create a circle teaching_table with a diameter of 36.
"""
class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        self.diameter = diameter
        print("New circle with diameter: " + str(self.diameter))

# Create a circle teaching_table with diameter 36
teaching_table = Circle(36)
"""
9/14
Introduction to Classes
Instance Variables
9 min
We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, but why is there such a strong need to differentiate the two if each object can only have the methods and class 
variables
Preview: Docs Variables are used to store data that can be used and manipulated throughout a program.
 the class has? This is because each instance of a class can hold different kinds of data.
The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
Let’s say that we have the following class definition:
"""
"""
We can instantiate two different objects 
from
Preview: Docs Loading link description
 this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.
"""
class FakeDict:
  pass
  
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints This works! This too!

"""
#Task1

In script.py, we have defined a Store class. Create two objects from this store class, named alternative_rocks and isabelles_ices.
"""
"""
#Task2
Give them both instance attributes called .store_name. Set the .store_name of alternative_rocks to "Alternative Rocks". Set the .store_name of isabelles_ices to "Isabelle's Ices".
"""
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


"""
10/14
Instance 
variables
Preview: Docs Loading link description
and class variables are both accessed similarly in Python. This is no mistake — they are both considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object, Python will throw an AttributeError.
"""

class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints This text gets printed!

"""
What if we aren’t sure if an object has an attribute or not? 
hasattr()
Preview: Docs Loading link description
 will 
return
Preview: Docs Loading link description
 True if an object has a given attribute and False otherwise. If we want to get the actual value of the attribute, 
getattr()
Preview: Docs Loading link description
 is a Python function that will return the value of a given object and attribute. In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

The syntax and parameters for these 
functions
Preview: Docs Loading link description
 look like this:

hasattr(object, "attribute") has two parameters:

object: the object we are testing to see if it has a certain attribute
attribute: the name of the attribute we want to see if it exists
getattr(object, "attribute", default) has three parameters (one of which is optional):

object: the object whose attribute we want to evaluate
attribute: the name of the attribute we want to evaluate
default: the value that is returned if the attribute does not exist (note: this parameter is optional)
Calling those functions looks like this:
"""
hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
"""
Above, we checked if the attributeless object has the attribute .fake_attribute. Since it does not, hasattr() returned False. After that, we used getattr() to attempt to retrieve .other_fake_attribute. Since .other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.
"""
"""
#Task1
In script.py, we have a list of different data types: a dictionary, a string, an integer, and a list, all saved in the variable can_we_count_it.
For every element in can_we_count_it, check if the element has the attribute .count using the hasattr() function. If so, print the following line of code:
"""
"""
#Task2
Now let’s add an else statement for the elements that do not have the attribute .count. In this else statement add the following line of code:
"""
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

"""
Let’s go over the terminal output of the past two instructions. You should see the following output in your terminal right now:

<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!

Copy to Clipboard

This is because dictionaries and integers both do not have a .count attribute, while strings and lists do. In this exercise, we have iterated through can_we_count_it and used hasattr() to determine which elements have a .count attribute. We never actually used the .count() method, but you can read more about it in the 
Python list count() documentation
Preview: Docs Returns the number of occurrences of a specified element in a list.
 if you are curious about what it is.

Select “Run” to move on to the next exercise!
"""