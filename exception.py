"""
try:
    print(2/0)
except:
    print("Cant divide by zero")

print("Execution continues... ")
"""
""" 
try:
    print(2/0)
except ZeroDivisionError as e:
    print(e) #shows error message

else :
    print("No error occured")

    """
""" 
try:
    print(12/2)
except ZeroDivisionError as e:
    print(e) #shows error message

else : #executes if no erorrs
    print("No error occured")
    """

try:
    print(2/0)
except:
    print("Cant divide by zero")
finally:
    print("Code continues...") #executes alongside the except function 

