name = " JOHn  ."

the_name=name.lower().strip(" ")[0:5]

print(the_name)


sentence_one = "The Dog Breed is German Shepherd"
sentence_a=sentence_one[8:23]

print(sentence_a)

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
sentence_b=sentence_two[16:29]

print(sentence_b)


tsentence = "The lazy dog;ran so fast;it hit the wall"
lsen = tsentence.split(";")
print(lsen)
print(len(lsen))        

first_name= "  Joh.n"  
last_name= "   Do,e"

fname = first_name.strip(" ")
print(fname)
f_name = fname[0:3] + fname[4:5]
print(f_name)
lname = last_name.strip(" ")
print(lname)
l_name = lname[0:2] + lname[3:4]
print(l_name)

fullname = f_name + " " + l_name
print(fullname)