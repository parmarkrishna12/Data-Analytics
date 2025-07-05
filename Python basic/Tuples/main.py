a=("Apple","Banana","Grapes",1,67,1,23)
print(type(a))

a=("Oneplus","Realme","Redmi","Nokia","Vivo")
print(a[0:2])
print(a[::2])#Gapvalue
print(a[::-1])#Reverse

#Iteration

#With for loop
for i in a:
    print(i)

#For loop with range and length in for loop
for i in range(len(a)):
    print(a[i])

# Along with while loop
i=0
while i<len(a):
    print(a[i])
    i+=1

a=("bmw","Audii","Porsche")
print("Before Conversion : ",type(a))

a=list(a)
print("After Conversion : ",type(a))

# Now we can manipulate the elements

a.append("Supra")
print(a)

#Index
print(a.index("bmw"))