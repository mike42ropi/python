daysoftheweek = ("Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday")


x = list(daysoftheweek)
x[3]="Thur"
daysoftheweek = tuple(x)
print("Monday" not in daysoftheweek)
