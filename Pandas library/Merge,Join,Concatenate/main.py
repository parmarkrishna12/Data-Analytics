import pandas as pd
data1 = {"Emp id":["E01","E02","E03","E04","EO5"],
        "Name":["krishna","Jainam","heet","hemali","bijal"],
        "Age":["18","29","14","32","49"]}
data2 = {"Emp id":["E01","E02","E03","E04","EO5"],
         "Salary":["30000","40000","10000","25000","50000"]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
#merge
print(pd.merge(df1,df2,on="Emp id"))#it will merge on emp id
print(pd.merge(df1,df2,on="Emp id",how="left"))#based on the left table
print(pd.merge(df1,df2,on="Emp id",how="right"))#based on right table


#concate
import pandas as pd
data1 = {"Emp id":["E01","E02","E03","E04","EO5"],
        "Name":["krishna","Jainam","heet","hemali","bijal"],
        "Age":["18","29","14","32","49"]}
data2 = {"Emp id":["E06","E07","E08","E09","E1O"],
         "Name":["sania","nihar","hello","akshita","het"],
        "Age":["17","19","15","22","39"]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(pd.concat([df1,df2]))