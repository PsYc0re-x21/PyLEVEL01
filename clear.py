user= {"name": "Root", "id": "6767", "Pass": "rootuser"}
backup= user.copy()
user01= {"name": "Joy", "id": "212", "Pass": "psycrow"}
print(f"User variable type is: {type(user)}")
print(f"Length of the user is: {len(user)}")

print(f"Keys in the dictionaries are: {user.keys()}")
print(f"Values in the dictionaries are: {user.values()}")
print(f"Items in the dictionaries are: {user.items()}")


print(f"Initial user infos: {user}")
user.clear()
print(f"User after clearing function: {user}")

user.update({"Address": "192.168.0.67", "port": "6767"})
print(f"User after updating function: {user}")
user.update(user01)
print(f"New user list after merging: {user}")
user.popitem() #only removes last item of dict
print(f"User after popping last item: {user}")
user.pop("id")
print(f"User after removing/popping id: {user}") 