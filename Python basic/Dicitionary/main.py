Employee={"name":"Jhon",
          "age":24,
          "gender":"male"}
print(Employee)

#To access a particular element
print(Employee["name"])

#Iteration in Dictionaries
Student={"Name":"krishna parmar",
         "Roll number":23,
         "Gender":"Female"}

#Printing all the key names one by one
for x in Student:
    print(x)

#Printing all the value names one by one
for x in Student:
    print(Student[x])

#Using Value function
for x in Student.values():
    print(x)

#Using items function
for x,y in Student.items():
    print(x,"=",y)


#Get
x=Student.get("Name")
print(x)

#item
a=Student.items()
print(a)

#Keys
b=Student.keys()
print(b)

#Values
c=Student.values()
print(c)

#copy
d=Student.copy()
print(d)

#setdefault
x=Student.setdefault("Roll number",23)
print(x)