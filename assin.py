trainees =  ["John", [2, ["James","Mary"]]]
#1. Display 2 using index, from the list.
print(trainees[1][0])

bas = trainees[1][0]
print(bas)

#2. Output James  using index, from the list.trainees.append(56)print(trainees)


mary = trainees[1][1][0]

print(mary)

#3. Using a method add 56 at the end of the list.trainees.append(56)

v = ["56"]
add = trainees.__add__(v)
print(add)

#4. Using a method add the name Mike between James and Marytrainees[1][1].insert(1, 'Mike')print(trainees)

add[1][1].insert(1,"Mike")
print(add)

#5. Change the value of 2 to 8trainees[1][0] = 8print(trainees)

add[1]=8
print(add)

#6. Remove John and Mary from the listtrainees.remove('John')print(trainees)

add.remove("John")
print(add)

#7. Using a function, determine the length of the list
k =len(add)
print(k)


train =  ["John","ford" ,[2, ["James","Mary"]]]
pp= ["j","u","y"]
uu= ["l","m","n"]
trains= train+pp+uu
print(trains)

trains.remove("ford")
print(trains)

trains.pop()
print(trains)

#del trains

trains.clear
print(trains)




car1 =input("Enter car names:")
car2 =input("Enter car names:")
car3 =input("Enter car names:")

models = []

models.append(car1)
models.append(car2)
models.append(car3)
print(models)
models.remove("merc")

print(models)