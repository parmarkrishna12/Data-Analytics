a={"Ironman","Hulk","Spiderman"}
print(a)
print(type(a))

for x in a:
    print(x)
a={"Ironman","Hulk","Spiderman"}

#Add
a.add("Captain America")
print(a)

#pop
a.pop() #RANDOM ELEMENT REMOVAL
print(a)

#remove
a.remove("Hulk") #PARTICULAR ELEMENT REMOVAL
print(a)

#Copy
b=a.copy()
print(b)