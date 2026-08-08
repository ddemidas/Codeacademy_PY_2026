'''
Learn Python: Files
Reading a File
7 min
Computers use file systems to store and retrieve data. Each 
file
Preview: Docs Loading link description
 is an individual container of related information. If you’ve ever saved a document, downloaded a song, or even sent an email you’ve created a file on some computer somewhere. Even script.py, the Python program you’re editing in the learning environment, is a file.

So, how do we interact 
with
Preview: Docs Loading link description
 files using Python? We’re going to learn how to read and write different kinds of files using code. Let’s say we had a file called real_cool_document.txt with these contents:

real_cool_document.txt

'''

'''
Wowsers!
'''

'''
We could read that file like this:

script.py
'''

with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)

'''
This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. Then we print cool_contents, which outputs the statement Wowsers!.
'''
with open('welcome.txt') as text_file:
  content_read = text_file.read()
  text_data = text_file.read()
print(content_read)
print(text_data)

'''
Learn Python: Files
Iterating Through Lines
5 min
When we read a file, we might want to grab the whole document in a single string, like 
.read()
Preview: Docs Loading link description
 would 
return
Preview: Docs Ends a function and sends a value back to the caller.
. But what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line instead of having the whole thing. Suppose we have a file:

keats_sonnet.txt
'''

'''
To one who has been long in city pent,
’Tis very sweet to look into the fair
And open face of heaven,—to breathe a prayer
Full in the smile of the blue firmament.
'''

with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)


   
'''
Task1
1.Using a with statement, create a file object pointing to the file how_many_lines.txt. Store that file object in the variable lines_doc.
'''
with open('how_many_lines.txt') as lines_doc:
  content = lines_doc.readlines()
  for line in content:
    print(line)

'''
Learn Python: Files
Reading a Line
5 min
Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, 
.readline()
Preview: Docs Returns the first line of content from an open file.
, which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls to .readline() will not throw an error but will start returning an empty string (""). Suppose we had this file:

millay_sonnet.txt
'''

'''
I shall forget you presently, my dear,
So make the most of this, your little day,
Your little month, your little half a year,
Ere I forget, or die, or move away,
'''

with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)
 
'''
Learn Python: Files
Writing a File
5 min
Reading a file is all well and good, but what if we want to create a file of our own? With Python we can do just that. It turns out that our 
open()
Preview: Docs Loading link description
 function that we’re using to open a file to read needs another argument to open a file to write to.

script.py
'''

with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")

'''
Here we 
pass
Preview: Docs Loading link description
 the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

This code creates a new file in the same folder as script.py and gives it the text What an incredible file!. It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.'''

'''
Task1
1. Create a file object for the file bad_bands.txt using the open() function with the w argument. Assign this object to the temporary variable bad_bands_doc.
'''
with open("bad_bands.txt", 'w') as bad_bands_doc:
  bad_bands_doc.write("I am the first written file")
  print(bad_bands_doc)
'''
Task2
2. Use the bad_bands_doc.write() method to add the name of a musical group you dislike to the document bad_bands.
'''
with open("bad_bands.txt") as obj_verif:
  var_obj_verif = obj_verif.read()
  print(var_obj_verif)
  
'''
Learn Python: Files
Appending to a File
6 min
So maybe completely deleting and overwriting existing files is something that bothers you. Isn’t there a way to just add a line to a file without completely deleting it? Of course there is! Instead of opening the file using the argument 'w' for write-mode, we open it 
with
Preview: Docs Loading link description
 'a' for append-mode. If we have a generated file with the following contents:

generated_file.txt
'''

'''
This was a popular file...
'''

'''
Then we can add another line to that file with the following code:
'''

with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("\n... and it still is")

'''
In the code above we open a file object in the temporary variable gen_file. This variable points to the file generated_file.txt and, since it’s open in append-mode, adds the string \n... and it still is to the file. The newline character \n moves to the next line before adding the rest of the string. If you were to open the file after running the script it would look like this:
'''

'''
This was a popular file...
... and it still is
'''

'''
Notice that opening the file in append-mode, with 'a' as an argument to 
open()
Preview: Docs Opens a file and returns a file object used for reading, writing, or appending data.
, means that using the file object’s 
.write()
Preview: Docs Loading link description
 method appends whatever is passed to the end of the file. If we were to run script.py again, this would be what generated_file.txt looks like:

generated_file.txt
'''

'''
This was a popular file...
... and it still is
... and it still is
'''

'''
Notice that we’ve appended "\n... and it still is" to the file a second time! This is because in script.py we opened generated_file.txt in append-mode.
'''

'''
1. We’ve got a file, cool_dogs.txt, filled with all the cool dogs we know. Somehow while compiling this list we forgot about one very cool dog. Let’s fix that problem by adding him to our cool_dogs.txt.

Open up our file cool_dogs.txt in append-mode and assign it to the file object cool_dogs_file.
'''

print("before changes")
with open("cool_dogs.txt") as obj_verif:
  var_obj_verif = obj_verif.read()
  print(var_obj_verif)

print("=========")
print("doing changes")
with open("cool_dogs.txt", 'a') as cool_dogs_file:
  cool_dogs_file.write("\n Air Buddy\n")
  print(cool_dogs_file)

print("=========")
print("after changes")
with open("cool_dogs.txt") as obj_verif:
  var_obj_verif = obj_verif.read()
  print(var_obj_verif)
  
'''
Learn Python: Files
What's With "with"?
6 min
We’ve been opening these files 
with
Preview: Docs Loading link description
 this with block so far, but it seems a little weird that we can only use our file variable in the indented block. Why is that? The with keyword invokes something called a context manager for the file that we’re calling 
open()
Preview: Docs Loading link description
 on. This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

Why is closing the file so complicated? Well, most other aspects of our code deal with things that Python itself controls. All the 
variables
Preview: Docs Variables are used to store data that can be used and manipulated throughout a program.
 you create: integers, 
lists
Preview: Docs Loading link description
, 
dictionaries
Preview: Docs Loading link description
 — these are all Python objects, and Python knows how to clean them up when it’s done with them. Since your files exist outside your Python script, we need to tell Python when we’re done with them so that it can close the connection to that file. Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file.

The with syntax replaces older ways to access files where you need to call 
.close()
Preview: Docs Loading link description
 on the file object manually. We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards.
'''

fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()


'''
1.
In script.py there’s a file object that doesn’t get closed correctly. Let’s fix it by changing the syntax!

Remove this line:

close_this_file = open('fun_file.txt')

Copy to Clipboard

And change it to use the with syntax from our previous exercises.

Remember to indent the rest of the body so that we don’t get an IndentError.
'''

#print("before changes")

with open('fun_file.txt') as close_this_file:
#with open('fun_file.txt') as obj_verif:
  #var_obj_verif = obj_verif.read()
  setup = close_this_file.readline()
  print("setup")
  print(setup)
  punchline = close_this_file.readline()
  print("punchline")
  print(punchline)

#close_this_file = open('fun_file.txt')


#setup = close_this_file.readline()
#punchline = close_this_file.readline()

#print(setup)
#print(punchline)
"""
Learn Python: Files
What Is a CSV File?
5 min
Text files aren’t the only things that Python can read, but they’re the only things that we don’t need any additional parsing library to understand. A 
CSV
Preview: Docs Loading link description
file is an example of a text file that imposes a structure on its data. CSV stands for Comma-Separated Values, and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format. A spreadsheet might look like the following:

Name	Username	Email
Roger Smith	rsmith	wigginsryan@yahoo.com
Michelle Beck	mlbeck	hcosta@hotmail.com
Ashley Barker	a_bark_x	a_bark_x@turner.com
Lynn Gonzales	goodmanjames	lynniegonz@hotmail.com
Jennifer Chase	chasej	jchase@ramirez.com
Charles Hoover	choover	choover89@yahoo.com
Adrian Evans	adevans	adevans98@yahoo.com
Susan Walter	susan82	swilliams@yahoo.com
Stephanie King	stephanieking	sking@morris-tyler.com
Erika Miller	jessica32	ejmiller79@yahoo.com

Notice that the first row of the CSV file doesn’t actually represent any data, just the labels of the data that’s present in the rest of the file. The rest of the rows of the file are the same as the rows in the spreadsheet software, just instead of being separated into different cells, they’re separated by… well, I suppose it’s fair to say they’re separated by commas.
"""

"""
Task1
 CSV files are just plain text files!

Open logger.csv using our standard with syntax, saving the file object in the temporary variable log_csv_file.

Task2
Print out the contents of logger.csv by calling .read() on the file. Notice that it is parsed as a string.
"""
with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())
"""
8/13
Learn Python: Files
Reading a CSV File
12 min
Recall our CSV file 
from
Preview: Docs Used to import specific attributes, classes, or functions from a Python module.
 our last exercise:
"""
"""
users.csv

Name, Username, Email
Roger Smith,rsmith,wigginsryan@yahoo.com
Michelle Beck,mlbeck,hcosta@hotmail.com
Ashley Barker,a_bark_x,a_bark_x@turner.com
Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
"""
"""
Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes. In Python, we can convert that data into a dictionary using the csv library’s DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the table:
"""
import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])


"""
9/13
Learn Python: Files
Reading Different Types of CSV Files
12 min
I need to level 
with
Preview: Docs Loading link description
 you. I’ve been lying to you for the past two exercises. Well, kind of. We’ve been acting like CSV 
files
Preview: Docs Loading link description
 are Comma-Separated Values files. It’s true that CSV stands for that, but it’s also true that files that use other separators are considered valid CSV files these days.

People used to call Tab-Separated Values files TSV files, but as other separators grew in popularity, everyone realized that creating a new .[a-z]sv file format for every value-separating character used is not sustainable.

So we call all files with a list of different values CSV files and then use different delimiters (like a comma or a tab) to indicate where the different values start and stop.

Let’s say we had an address book. Since addresses usually use commas in them, we’ll need to use a different delimiter for our information. Since none of our data has semicolons (;) in it, we can use those.

addresses.csv
"""
"""
Name;Address;Telephone
Donna Smith;126 Orr Corner Suite 857\nEast Michael, LA 54411;906-918-6560
Aaron Osborn;6965 Miller Station Suite 485\nNorth Michelle, KS 64364;815.039.3661x42816
Jennifer Barnett;8749 Alicia Vista Apt. 288\nLake Victoriaberg, TN 51094;397-796-4842x451
Joshua Bryan;20116 Stephanie Stravenue\nWhitneytown, IA 87358;(380)074-6173
Andrea Jones;558 Melissa Keys Apt. 588\nNorth Teresahaven, WA 63411;+57(8)7795396386
Victor Williams;725 Gloria Views Suite 628\nEast Scott, IN 38095;768.708.3411x954
"""
"""
Notice the \n character, the escape sequence for a new line. The possibility of a new line escaped by a \n character in our data is why we 
pass
Preview: Docs Loading link description
 the newline='' keyword argument to the 
open()
Preview: Docs Loading link description
 function.

Also, notice that many of these addresses have commas in them! This is okay; we’ll still be able to read it. If we wanted to, say, print out all the addresses in this CSV file, we could do the following:
"""

import csv

with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])

'''
Notice that when we call csv.DictReader(), we pass the delimiter argument, which is the string that’s used to delineate separate fields in the CSV. We then iterate through the CSV and print out each of the addresses.
'''

#My solution:
#Task1
#Import the csv module.
#Task2
#Open the file books.csv as the variable books_csv.
#Task3
#Create a DictReader instance that uses the @ symbol as a delimiter to read books_csv. Save the result in a variable called books_reader.
import csv
isbn_list = []
with open('books.csv') as books_csv:
  print("=====================")
  #print("File as it is:")
  #print(books_csv.read())
  print("=====================")
  books_reader = csv.DictReader(books_csv, delimiter='@')
  print("variable books_reader:")
  print(books_reader)
  #for item in books_reader:
    #print(item)
#Task4
#Create a list called isbn_list, and iterate through books_reader to get the ISBN number of every book in the CSV file. Use the ['ISBN'] key for the dictionary objects passed to it.
  print("=====================")
  for book in books_reader:
    #isbn_list = [book['ISBN'] for book in books_reader]
    isbn_list.append(book['ISBN'])
    #isbn_list = item['ISBN']

print('ISBN list:')
print(isbn_list)

  
  
print("=====================")






#Codeacademy's solution:
import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]
  

"""
10/13
Learn Python: Files
Writing a CSV File
14 min
Naturally, if we have the ability to read different CSV 
files
Preview: Docs Files are named locations on disk to store related information that can be used in Python.
, we might want to be able to programmatically create CSV files that save output and data that someone could load into their spreadsheet software. Let’s say we have a big list of data that we want to save into a CSV file. We could do the following:

"""

big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)


"""
In the example code, we had a set of 
dictionaries
Preview: Docs Loading link description
 
with
Preview: Docs Loading link description
 the same keys for each, a prime candidate for a CSV. We import the csv library, and then open a new CSV file in write mode by passing the 'w' argument to the 
open()
Preview: Docs Opens a file and returns a file object used for reading, writing, or appending data.
 function.

We then define the fields we’re going to be using in a variable called fields. We then instantiate our CSV writer object and 
pass
Preview: Docs Loading link description
 two arguments. The first is output_csv, the file handler object. The second is our list of fields fields, which we pass to the keyword parameter fieldnames.

Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First, we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file. Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as a key. We call output_writer.writerow() with the item dictionary, which writes each line to the CSV file.
"""

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

#Task1
#We have a list in the workspace access_log, which is a list of dictionaries we want to write out to a CSV file.Let’s start by importing the csv module.

import csv
#Task2
#Open the file logger.csv in the temporary variable logger_csv. Don’t forget to open the file in write mode.
#Task3
#Create a csv.DictWriter instance called log_writer. Pass logger_csv as the first argument and then fields as a keyword argument to the keyword fieldnames.
with open('logger.csv','w') as logger_csv:
  #fields = ['time','limit','address']
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)


"""
11/13
Learn Python: Files
Reading a JSON File
7 min
CSV isn’t the only file format that Python has a built-in library for. We can also use Python’s file tools to read and write 
JSON
Preview: Docs The `json` module is used for encoding and decoding objects to and from the JSON format.
. JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript. The name, like CSV, is a bit of a misnomer — some JSON is not valid JavaScript (and plenty of JavaScript is not valid JSON).

JSON’s format is very similar to Python dictionary syntax, and so JSON 
files
Preview: Docs Loading link description
 might be easy to read 
from
Preview: Docs Loading link description
 a Python developer’s standpoint. Nonetheless, Python comes 
with
Preview: Docs Loading link description
 a json package that will help us parse JSON files into actual Python 
dictionaries
Preview: Docs Loading link description
. Suppose we have a JSON file like the following:

purchase_14781239.json


"""

"""
{
  "user": "ellen_greg",
  "action": "purchase",
  "item_id": "14781239"
}

"""

"""
We would be able to read that in as a Python dictionary with the following code:

json_reader.py
"""

import json

with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# Prints 'ellen_greg'

#Task1
#Let’s read a JSON file! Start by importing the json module.

import json

"""
#Task2
Open up the file message.json, saving the file object to the variable message_json.

Open the file in read mode, without passing any additional arguments to open().

#Task3
Pass the JSON file object as an argument to json.load() and save the resulting Python dictionary as message.
#Task4
Print out message['text']
"""

with open('message.json') as message_json:
  message = json.load(message_json)

  print(message['text'])
  
"""
12/13
Learn Python: Files
Writing a JSON File
5 min
Naturally, we can use the json library to translate Python objects to JSON as well. This is especially useful in instances where we’re using a Python library to serve web pages; we would also be able to serve JSON. Let’s say we had a Python dictionary we wanted to save as a JSON file:
"""

turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

"""
We’d be able to create a JSON file 
with
Preview: Docs Loading link description
 that information by doing the following:
"""



import json

with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)

"""
We import the json module, open up a write-mode file as the variable json_file, and then use the 
json.dump()
Preview: Docs Loading link description
 function to write to the file. json.dump() takes two arguments: first the data object, then the file object we want to save.
"""

"""
#Task1
In your workspace, we’ve put a dictionary called data_payload. We want to save this to a file called data.json.

Let’s start by importing the json library.
"""
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

"""
#Task2
Open a new file object and assign it to the variable data_json. The filename should be 'data.json', and the file should be opened in write mode.
"""
"""
#Task3
Call json.dump() with data_payload and data_json to convert our data to JSON and then save it to the file data.json.
"""
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)

"""
Learn Python: Files
Review

Now we know all about files! We were able to:

Open up file objects using 
open()
Preview: Docs Loading link description
 and 
with
Preview: Docs Loading link description
.
Read a file’s full contents using Python’s .read() method.
Read a file line by line using 
.readline()
Preview: Docs Loading link description
 and .readlines().
Create new files by opening them in write mode.
Append to a file non-destructively by opening a file in append mode.
Apply all of the above to different types of data-carrying files, including CSV and JSON!
We have all the skills necessary to read, write, and update files programmatically, a very useful set of skills in the Python universe!
"""


with open('file.txt') as file_object:
  print(file_object.read())

"""
Thank you for learning about files in Python with us!
"""