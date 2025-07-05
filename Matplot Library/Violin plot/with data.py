import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
plt.violinplot(df["Annual Salary"],showmeans=True)
plt.show()