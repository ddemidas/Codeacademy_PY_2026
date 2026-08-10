"""
Hacking the Fender
The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords, including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender’s systems, and you must update his passwords.csv file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if he viewed Slash Null as a threat.

Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.

If you get stuck during this project, check out the project walkthrough video, which can be found in the help menu.
"""

"""
#Task1
Are you there? We’ve opened up a communications link to The Fender’s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called passwords.csv.
First, import the csv module, since we’ll be needing it to parse the data.
"""
import csv
"""
#Task2
We need to create a list of users whose passwords have been compromised. Create a new list and save it to the variable compromised_users.
"""
compromised_users = []
"""
#Task3, #Task4, #Task5, #Task6, #Task7
Next, we’ll need you to open up the file itself. Store it in a file object called password_file.
Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
Now we’ll want to iterate through each of the lines in the CSV.
Create a for loop and save each row of the CSV into the temporary variable password_row.
Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised.
Run your code. Do you see a list of usernames?
Remove the print() statement. We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to compromised_users instead of printing it.
"""
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file, delimiter = ',')
  for row in password_csv:
    compromised_users.append(row['Username'])
print(compromised_users)

"""
#Task8, #Task9, #Task10, #Task11
Exit out of your with block for passwords.csv. We have all the data we need from that file.
Start a new with block, opening a file called "compromised_users.txt". Open this file in write mode, saving the file object as compromised_user_file.
Inside the new context-managed block opened by the with statement, start a new for loop.
Iterate over each of your compromised_users.
Write each username in compromised_users to compromised_user_file.
Exit out of that with block. You’re doing great so far! We’ve got the data we need to employ as insurance against The Fender.
"""
import csv
compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file, delimiter = ',')
  for row in password_csv:
    compromised_users.append(row['Username'])
print(compromised_users)

with open('compromised_users.txt','w') as compromised_user_file:
  for item in compromised_users:
    compromised_user_file.write(item+"\n")

with open('compromised_users.txt') as obj_verif:
  var_verif = obj_verif.read()
  print(var_verif)

"""
#Task12, #Task13, #Task14, #Task15
Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.
First, we’ll need to import the json module.
Open a new JSON file in write mode called "boss_message.json". Save the file object to the variable boss_message.
Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict.
Give it a "recipient" key with a value "The Boss".
Also give it a "message" key with the value "Mission Success".
Write out boss_message_dict to boss_message using json.dump().
"""
with open('boss_message.json', 'w') as boss_message:
  json.dump(boss_message_dict, boss_message)

with open('boss_message.json') as obj_verif2:
  var_verif2 = json.load(obj_verif2)

print(var_verif2)

"""
#Task16, #Task17, #Task18, #Task19
Now that we’ve safely recovered the compromised users, we’ll want to overwrite the passwords.csv file with new contents. Create a new with block and open passwords.csv in replace mode. Save the file object to a variable called new_passwords_obj.
The Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature; whenever he hacks someone, he adds this signature to one of the files he touches. Here is the signature:
Write slash_null_sig to new_passwords_obj. Now the original passwords.csv has been replaced with the decoy content!
What an incredible success! We’ll take care of moving the new passwords file over the old one in case you want to practice hacking The Fender in the future.
Thank you for your service, programmer.
"""
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

"""
with open('passwords.csv','r') as new_passwords_obj:
 new_passwords_obj = slash_null_sig
 print(new_passwords_obj)