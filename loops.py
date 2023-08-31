# x = list(range(2,77))
# print(x)

# # for numbers1 in range(1,6):
# #     print(numbers1)

# numbers=[2,3,4,5,6,7,8,9]
 
# sum_of_numbers = 0
# lol = []
# for i in numbers:
#     sum_of_numbers +=(i)
# lol.append(sum_of_numbers)

    
# print(lol)
# 99% of loop will be stored in accessing inside list/tuple

# numbers=range(2,40)
# five=[] 
# rest=[]
# seven = []
# for i in numbers:
#     if i%7==0:
#         seven.append(i)
#     elif i%5==0:
#         five.append(i)
#     else:
#         rest.append(i)
# print(seven)
# print(five)
# print(rest)

# store only the first 10  odd numbers between 0-50

count=1
for i in range(0,51):
    if (i%2!=0):        
        print(i)
        count=count+1
        

    if count==10:
        break
    else:
       pass

