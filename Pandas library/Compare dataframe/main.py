import pandas as pd
data = {"Fruits":["Mango","Apple","banana","Orange"],
        "price":["100","50","60","70"],
        "Quantity":["15","20","25","30"]}
df = pd.DataFrame(data)
print(df)

df1 = df.copy(data)
print(df1)
#change the dataframe as mention
df1.loc[0,"price"]="120"
df1.loc[1,"price"]="130"
df1.loc[3,"price"]="140"
df1.loc[2,"Quantity"]="15"
df1.loc[1,"Quantity"]="30"
print(df1)

#compare
print(df.compare(df1,align_axis = 0))
print(df.compare(df1,keep_equal = True))
print(df.compare(df1,keep_shape = True))