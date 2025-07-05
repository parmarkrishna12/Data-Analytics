import matplotlib.pyplot as plt
x = ["Vivo","iphone","oppo","oneplus","redmi"]
y = [22,35,50,30,10]
c = ["red","blue","green","yellow","orange"]
ex= [0,0,0,0,0.1]
plt.pie(y,labels=x , colors=c,explode=ex,shadow=True,autopct="%1.1f%%")
plt.show()