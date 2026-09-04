import datetime
x = datetime.datetime.now()
year = x.year
month = x.month
print(x.strftime("%A, %d %B, %Y"))

# %A = Weekday, %B = Month name, %d = Day of month, %Y = Year, %H = Hour, %M = Minute, %S = Second