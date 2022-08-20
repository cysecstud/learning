#!/usr/bin/python3

import re
#imports regular expression which is a string of
#characters to be searched for in a longer piece of text

from pwn import *

print("This will check your Password Strength!")
print("It will first check a wordlist then give you a rating 1-5\n")

password = input("Enter Password: ")


def check_common_passwords():

    wordlist = "/usr/share/SecLists/Passwords/xato-net-10-million-passwords-1000000.txt" #set to wordlist to check your password

    with open(wordlist, "r") as password_list: #open a wordlist in READ mode and set variable 'password list'
        for i in password_list: #iterate through the passwords
    	    if i == password:
                print("\n- Your password was found in the wordlist supplied\n")
                return #breaks out of the for loop because password match was found
        print("\n- Your password was not found in the supplied wordlist\n")



def password_strength():

    ticker = 0
    
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
        print("- Your password should have atleast 12 characters\n")
    if len(password) <= 8:
        ticker = ticker - 1

    print("- Your password strength is a: {}".format(ticker))


check_common_passwords()
password_strength()

