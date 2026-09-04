a = {12,34,65,23,25,212003}
b = {456,345,567,234,212003}
c=a.intersection(b)
d=a.union(b)
a.add(67)
a.update([987,4564,345,45])
a.pop()
a.discard(67)
print(f"Intersection of a and b is: {c}")
print(f"Union of a and b is: {d}")