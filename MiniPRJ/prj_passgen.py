#~~~VERSION-01~~~#
"""import random

def pass_gen(passlen):
    password= "" #random module will take care of it
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+_-"
    for i in range(1, passlen+1):
        password = password + random.choice(charset)
        print(password) 


passlen= int(input("Enter password length: "))
pass_gen(passlen)"""


#~~~VERSION-02~~~#
import random

def pass_gen(passlen):
    password= "" #random module will take care of it
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW_XYZ0123456789+_-"
    for i in range(1, passlen+1):
        password = password + random.choice(charset)
    return password
    


passlen= int(input("Enter password length: "))
passcount= int(input("Enter how many password combinations you want: "))
if passlen<8:
    print("Password length must be 8 characters long. Please try again!")
    exit()
for i in range(1,passcount+1):

    password= pass_gen(passlen)
    print(password.upper())

