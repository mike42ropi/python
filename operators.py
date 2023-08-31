x= 19
# if (x=18)and (x>18):
# print
#   

if  (x > 18):
  print("Can vote")
else:
 print("Cannot vote")


num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
num3 = int(input("Enter a number"))

if (num1>num2) and (num1>num3):
  print("The largest is:" + num1)
elif (num2>num1) and (num2>num3):
  print("The largest is:" + num2 )
elif (num2==num1) and (num2==num3):
  print("The largest is "+ num1, num2 , num3 )
else:
 print("The largest is "+ num3)




