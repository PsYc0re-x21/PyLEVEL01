num1 = int(input("Enter first number: "))
num2= int(input("Enter second number: "))

print(
"Press 1 for addition \n" \
"Press 2 for Substraction \n" \
"press 3 for Division \n" \
"Press 4 for Multiplication")
choice = input()

def add(a, b):
    print("Addition is: ", a+b)
def sub(a, b):
    print("Substraction is: ", a-b)
def div(a, b):
    print("Division is: ", a/b)
def mul(a, b):
    print("Multiplication is: ", a*b)

if choice=="1":
    add(num1, num2)
elif choice=="2":
    sub(num1, num2)
elif choice=="3":
    div(num1, num2)
elif choice== "4":
    mul(num1,num2)
else:
    print("Please select valid value!")

    