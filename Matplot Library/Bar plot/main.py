import matplotlib.pyplot as plt
y = [98,45,67,43,21]
x=["part1","part2","part3","part4","part5"]
colors = ["blue","green","red","purple","orange"]
plt.bar(x,y,color= colors,edgecolor='black')
plt.xlabel("Parts of harry potter")
plt.ylabel("Populartity")
plt.title("Bar plot",fontsize=20)
plt.show()


