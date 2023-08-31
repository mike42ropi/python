my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

print(my_ds[3][2]["currency"]) 
my_ds[3][2]["amount"]=90
print(my_ds)

# v =int(str( my_ds[4])[::-1])
# print(v)

l=my_ds[4]
rs = str(l)[::-1]
my_ds[4]=int(rs)
print(my_ds)


# u ={"name" : "John Doe", "age":30, "location": 100, "email" :"johndoe@mail.com"}
# u.[
                                                                                                                                                                                                                                                                                                                                                      
# print(u)