
'''
task4
'''
#we need to import a module responsible for generating random numbers
import random
'''
task1

In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
'''
'''
task2

Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
'''
'''
task3

We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
'''
#a very simple answer before the logic of random answers has been established, can be commented or removed
#answer = "Yes"
'''
task5
Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:
'''
#here we specify the range of random numbers taking part in the game
random_number = random.randint(0,9)
primer="A random number for this round is: "
print(str(primer) + str(random_number))
'''
task6
Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!

For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely”
'''
'''
task7
Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

Recall that the 9 possible answers of the Magic 8-Ball are:

Yes - definitely

It is decidedly so

Without a doubt

Reply hazy, try again

Ask again later

Better not tell you now

My sources say no

Outlook not so good

Very doubtful
'''
'''
task8
Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.
'''
'''
task9
Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format:
'''
'''
task10
Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:

Magic 8-Ball's answer: [answer]

Copy to Clipboard

For example, when running the program it should look something like:

Magic 8-Ball's answer: My sources say no

'''



#setting up an appendix to an answer
answer_format="Magic 8-Ball's answer: "

#here we specify the question to the fortune telling ball
#in order to make question_trigger True:
question = "Will the weather be good tomorrow?"
      #OR#
#in order to make name_trigger False:
#question = ""
#debugging: we are showing the length of players question:
print("The length of players question is: "+str(len(question))+" characters")
#a variable to catch if the players question is empty or not
question_trigger = len(question)>0
#debugging: a piece of code to see if the question is empty or not
if question_trigger == True:
  print("question_trigger is "+str(question_trigger))
else:
  print("question_trigger is "+str(question_trigger))

#piece of code to describe scenarious of output specially for the case when the players question is empty:
match question_trigger:
  case False:
    random_number = random_number+10
    print ("Question can never be empty, further game is impossible, please leave the casino immediately.")
    #break
  case True:
    print ("Your question is understood by Ball.")

#here we specify the name of the player once again according to the task13
#in order to make name_trigger True:
#name = "Dmytrii"
      #OR#
#in order to make name_trigger False:
name = ""
#debugging: we are showing the length of players name:
print("The length of player name is: "+str(len(name))+" characters")

#a variable to catch if the players name is empty or not
name_trigger = len(name)>0
#debugging: a piece of code to see if the name is empty or not
if name_trigger == True:
  print("name_trigger is "+str(name_trigger))
else:
  print("name_trigger is "+str(name_trigger))
#piece of code to describe scenarious of output depending on the fact if the players name is empty or not
match name_trigger:
  case False:
    print ("Question: " + str(question))
  case True:
    print(str(name)+" asks: " + str(question))
#logic of answer, printing out answer with an appendix making the answer corresponding to the format given by task10:
if random_number == 1:
  answer="Yes - definitely"
  print(str(answer_format)+str(answer))
elif random_number ==2:
  answer="It is decidedly so"
  print(str(answer_format)+str(answer))
elif random_number ==3:
  answer="Without a doubt"
  print(str(answer_format)+str(answer))
elif random_number ==4:
  answer="Reply hazy, try again"
  print(str(answer_format)+str(answer))
elif random_number ==5:
  answer="Ask again later"
  print(str(answer_format)+str(answer))
elif random_number ==6:
  answer="Better not tell you now"
  print(str(answer_format)+str(answer))
elif random_number ==7:
  answer="My sources say no"
  print(str(answer_format)+str(answer))
elif random_number ==8:
  answer="Outlook not so good"
  print(str(answer_format)+str(answer))
elif random_number ==9:
  answer="Very doubtful"
  print(str(answer_format)+str(answer))
elif random_number ==0:
  answer="Zero - please leave the casino"
  print(str(answer_format)+str(answer))
else:
  answer="Error"
  print(str(answer_format)+str(answer))
'''
task11
Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.

Run your program several times to see that it’s working as expected.
'''
#Optional Challenges
'''
task12
If you’re up for some more challenges, try implementing the following features to your program.

So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.

To do this, you will need to increase the range of randomly generated numbers and add additional elif statements for each new answer.
'''
'''
task13
What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

 asks: Will I win the lottery?
Magic 8 Ball's answer: Outlook not so good

Copy to Clipboard

As you can see, the formatting of the output can use some improvement when there is no name provided.

We can address this by printing out just the question, such that it looks like the following:

Question: Will I win the lottery?
Magic 8-Ball's answer: Outlook not so good

Copy to Clipboard

You can implement this by creating an if/else statement such that:

If the name is an empty string, it will only print the question.
Else, the player’s name and question are both printed.
'''

'''
task14
What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

To ensure that the fabric of reality is safe, we can create an if/else statement where:

If the question is an empty string, print out a message to the user.
Else, print the name and question, with the Magic 8-Ball’s answer.
'''
'''
task15
Don’t forget to check off all the tasks before moving on.
'''
