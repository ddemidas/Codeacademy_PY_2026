# we input our word here
usr_s = input("Please enter the word to be checked if it is a palindrome: ")

# we calculate the length of our input
length = len(usr_s)

# we perform integer division here with the operator double forward slash //
# mod division is being done with percentage sign %
# it is like div and mod in Pascal
# if number of characters in our word is odd (not even) then the obsolete middle character is unimportant
# the middle character will be equal to itself
half_length = length // 2


# we establish a boolean variable bool_checker in order to make logic operations transparent
# we are establishing a for loop with the amount of iterations equal to the half-length of our word
for i in range(half_length):
    bool_checker = (usr_s[i] != usr_s[-1 - i])
    # bool checker checks a symbol versus its polar brother in the opposite end of our word
    # pay attention: -1
    print(usr_s[i], usr_s[-1 -i])
    if (bool_checker == True):
        # boolean condition triggered, we should stop the program
        print("It's not a palindrome, the program has been terminated")
        #quit command performs the termination
        quit()

#If the loop is over without triggering bool_checker as True then our word is a palindrome
print("It's a palindrome")