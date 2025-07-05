import pandas as pd


df = pd.read_excel("C:/Users/krish/Downloads/ESD.xlsx")
print(df)
df.loc[(df["Bonus %"]==0),"Getbonus"] = "no bonus"
df.loc[(df["Bonus %"] > 0),"Getbonus"] = "bonus"
print(df.head(10))

df["Salary"]= (df["Annual Salary"]/100)*20
print(df.head(10))


data = pd.read_csv("C:/Users/krish/Downloads/People.csv")
print(data)
data["name"]=data["User Id"] +" " + data["Job Title"]
print(data)

data = {"Months":["January","feburary","March","April"]}
a=pd.DataFrame(data)
print(a)
def extract(values):
    return values[0:3]

a["Short_month"] = a["Months"].map(extract)
print(a)