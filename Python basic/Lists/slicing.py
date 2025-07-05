fruits=["apple","banana",12,14,15]
print(fruits)
print(type(fruits))

#SLICING LISTS
#Accessing the element
a=["Iron man","Hulk","Superman","Spider man"]
print(a[2])
print(a[1:3]) #Multiple elements accessing
print(a[::2]) #Skip the element
print(a[::-1]) #Reverse the list

l1=[20,30,40,50,60,70]
l2=[i for i in l1 if i>45] #List Comprehension
print(l2)