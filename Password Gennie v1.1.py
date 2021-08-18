""" This is attempt numero uno at a password generator
date : 30/03/2021
N.B: the 3 quote comments will indicate the date when new code
was added"""

""" Random function imported 31/03/2021"""
import random
#this should print a introductry message
print("We are going to be generating a password from your name and surname")

#our inputs, the .title capitalizes every word,
""" .title added in v1.1 31/03.2021"""

name = input("Please enter your name: ")
name.title()
surname = input("Please input your surname: ")
surname.title()

#our function that should take our inputs, slice them and return a password
def password_gen(name, surname):
#these are our characters that will be selected for our 6 digit password 
    char1 = name[0]
    char2 = name[2]
    char3 = surname[0]
    char4 = surname[2]
    char5 = surname[4]
    char6 = len(name+surname)
    password = char1 + char2 + char3 + char4 + char5 + str(char6)

    return password
"""v1 31/03/2021"""
print("Your password is: " + password_gen(name, surname))
