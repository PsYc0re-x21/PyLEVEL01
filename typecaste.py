# we have to convert tuples to list to modify them. 

a = (12,45,67,23,687,76)

a = list(a) 
print(type(a))
print(f"Length of the list is: {len(a)}")
print(f"Initial list: {a}")
#adding items to the tuples

a.insert(3,69)
print(f"Length of the final list is: {len(a)}")
print(f"Modified lsit: {a}")