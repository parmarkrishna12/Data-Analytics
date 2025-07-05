import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_excel("C:/Users/krish/Downloads/ESD.xlsx")
df = pd.DataFrame(data)
print(df)
plt.scatter(df["Age"],df["EEID"])
plt.show()