file = open(r"c:\Users\SH Joy\Downloads\Read Me.txt", "r")
lines = file.readlines()
print(lines[0], lines[1])

for i in lines[0:5]:
    print(i, end="")
file.closse()
# end prevents the default behaviour, which is to print a new line after each print statement. So it will print the lines as they are in the file.