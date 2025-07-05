import matplotlib.pyplot as plt
x = ["day1","day2","day3","day4","day5"]
y = [300,420,250,230,400]
y1 = [500,450,300,250,220]
plt.plot(x,y,marker = "d",ls = "--",color="red",label="week1")
plt.plot(x,y1,marker = "^",color="green",label="week2")
plt.legend()
plt.show()