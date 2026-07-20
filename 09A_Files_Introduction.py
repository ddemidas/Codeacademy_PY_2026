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
