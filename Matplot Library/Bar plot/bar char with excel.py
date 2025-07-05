import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Users/krish/Downloads/expense3.xlsx")
df = pd.DataFrame(data)
print(df)
grp = df.groupby("Payment Mode")["Amount"].sum()
print(grp)
plt.bar(grp.index,grp.values)
plt.show()