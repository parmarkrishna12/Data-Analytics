import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
df1 = (df.head(10))
plt.stem(df1["Annual Salary"],linefmt="--",markerfmt="o")
plt.show()