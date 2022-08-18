import re 
#imports regular expression which is a string of
#characters to be searched for in a longer piece of text

def password_strength():
    print("This will check your Password Strength!")
    ticker = 0
    password = input("Enter Password: ")
    
    if re.search('[a-z]',password): #uses the search function to check password for lowercase chars
        ticker = ticker +1
    if re.search('[A-Z]',password): #searches for uppercase characters
        ticker = ticker +1
    if re.search('[0-9]',password): #searches for numbers
        ticker = ticker +1
    if re.search('[!@#$%^&*()_+-=~`;,.<>]',password): #checks for special characters
        ticker = ticker +1
    if len(password) >= 12:
        ticker = ticker + 1
    else:
        print("Your password should have 12 characters")
    if len(password) <= 8:
        ticker = ticker - 1
    


    if (ticker <= 3):
        print(password + " is a very weak password")
    elif (ticker <= 4):
        print(password + " could be stronger")
    else:
        print("Congratz" + password + "is a strong password")
    
password_strength()
