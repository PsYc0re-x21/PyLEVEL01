# built in and manual modules are available. But will deal with built-in 
import random
import math
print(math.sqrt(36))
print(math.pow(2,3))
print(math.factorial(5))

print("### random ###")

print(random.randint(1,100))
print(random.randrange(1,10))


print("### Shuffle ###")

a = [1,2,56,34,23]
random.shuffle(a)
print(a)

print(" ### choice ###")
b = "233298wifjisdofr23"
print(random.choice(b))
