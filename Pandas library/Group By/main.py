import pandas as pd
data = pd.read_excel("C:/Users/krish/Downloads/ESD.xlsx")
print(data.head(5))

gp=data.groupby(["Department","Gender"]).agg({"EEID":"count"})
print(gp)

gp1=data.groupby("Country").agg({"Annual Salary":"max"})
print(gp1)

gp2=data.groupby(["Country","Gender"]).agg({"Annual Salary":"min"})
print(gp2)

