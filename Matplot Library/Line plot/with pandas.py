import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("C:/Users/krish/Downloads/expense3.xlsx")
df = pd.DataFrame(data)
print(df)
grp = df.groupby("Category") ["Amount"].sum()
print(grp)
plt.plot(grp.index.tolist(),grp.values)
plt.show()