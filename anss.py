# #  divisible by 7
numberx= int(input("Enter number"))

if  (numberx%7==0):
  print("Divisible by 7")
else:
 print("Not divisible by 7")


# # electricity bill

units = int(input("Enter a units"))

bill =0

if  (units>0  and units<=50):
  bill= ( units* 20)
elif (units>50 and units<=100):
 bill = (units*40)-1000 
else:
 bill=  (units*100)-4000
 
print(bill)

# 1.Given a variable temperature with a value of 25°C, 
# write an if statement to check if the temperature is above 30°C
# using the greater than (>) operator.

temprature = 30

if  (temprature>30):
  print("Temprature is above 30")

else:
 print("Temprature is below 30")


# 2.	Create a dictionary called stock with items as keys and their quantities as values.
#  Write an if-else statement to check if the quantity of "apples" is zero
#  using the equality (==) operator.

stock = {"bananas": 89 , "Mangoes":49, "Apples" : 55 }

if  (stock["Apples"])==0:
  print("yes")
else:
  print("no")


# 3.Declare a list called even_numbers containing integers. 
# Write an if statement to check if the first element of the 
# list is an even number using the modulo (%) operator 

even_numbers = [99,44,6,89.9,10]

if  (even_numbers[2]%2==0):
  print("even")
else:
  print("odd")




# 4.	Imagine you have a list employees containing dictionaries with keys "name", "hours_worked", 
# and "hourly_rate". Write a code snippet using  if statements to calculate the salary 
# for an employee named "Alice" based on her hours worked and hourly rate.

employees= [{"name": "Michael", "hours_worked1":"48",  "hourly_rate": "80"},
           {"name": "Alice", "hours_worked":"28",  "hourly_rate": "70"},
           {"name": "John", "hours_worked":"30",  "hourly_rate": "50"}
           ]


if ("Alice" in employees[1]["name"]):
    salary =int(employees[1]["hours_worked"])*int(employees[1]["hourly_rate"])
else:
    print("Alice is not in the list of employees.")
print("The salary is:", salary)

# 5.	Create a dictionary book_ratings with book titles as keys and their ratings as values. 
# Write an if-elif-else statement to find out if a book 
# "The Adventure" has a rating of 5 or is rated below 2.

book_ratings= {"LOHN":"5", 
               "Atomic Habits": "4",
               "The Adventure":"1" }

if int(book_ratings["The Adventure"])>4 and int(book_ratings["The Adventure"])<6:
  print("Rating is 5")

elif int(book_ratings["The Adventure"])<2:
  print("Rating below 2")

else:
  print("Rating is different")


# 6.	Suppose you have two sets: set_x and set_y. Write a code snippet using
#  conditional statements to check if the symmetric difference between the two sets
#  is not empty, using the ^ (symmetric difference) operator

set_x={ 9, "Saka", "Nairobi", (6,7,8), "kesho"}
set_y={ "Saka",9,  "Cape Town", ("book titles","LOHN","ratings","5",)}

set =set_x.symmetric_difference(set_y)

if len(set)==0:
  print("Empty")
else:
  print("Not empty")