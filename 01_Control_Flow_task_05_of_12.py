#Enter a user name here, make sure to make it a string
#Enter a user name in the field for user_name and try running the program.
user_name = "Dave"
#Set your user_name to be angela_catlady_87.
user_name = "angela_catlady_87"
#Update the program with a second if statement so it checks for Angela’s user name as well and prints
if user_name == "Dave":
  print("Get off my computer Dave!")
if user_name == "angela_catlady_87":
 print("I know it is you, Dave! Go away!")
 
#Using the above syntax, we can rewrite the code given in the switch-case example as shown below:

user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  
