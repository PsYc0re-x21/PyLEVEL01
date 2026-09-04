username= "root"
password= "admin"

name= input("Enter username: ")
passw= input("Enter password: ")

if name == username and passw==password:
    print("Authentication successfull!")

else:
    print("Wrong username or password")
