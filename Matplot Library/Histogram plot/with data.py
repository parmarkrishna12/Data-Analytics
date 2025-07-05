import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
plt.hist(df["Age"],bins=10,edgecolor="black",color="pink")
plt.show()