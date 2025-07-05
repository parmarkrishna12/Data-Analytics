import pandas as pd
#pivoting
dict = {"Keys":["k1","k2","k1","k2"],
        "Names":["John","ben","peter","david"],
        "Houses":["Green","blue","red","yellow"],
        "Grades":["3rd","2nd","1st","4th"]}
df = pd.DataFrame(dict)
print(df)
print(df.pivot(index = "Keys",columns = "Names",values = ["Houses","Grades"]))

#melting
dict1 = {"Names":["John","ben","peter","david"],
        "Houses":["Green","blue","red","yellow"],
        "Grades":["3rd","2nd","1st","4th"]}
df1 = pd.DataFrame(dict1)
print(df1)
print(pd.melt(df1,id_vars = ["Names"],value_vars = ["Houses","Grades"]))
