import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel("expense3.xlsx")
df = pd.DataFrame(data)
print(df)
grp = df.groupby(["Payment Mode"])["Amount"].sum()
print(grp)
plt.pie(grp.values,labels = grp.index,autopct="%1.1f%%")
plt.show()
