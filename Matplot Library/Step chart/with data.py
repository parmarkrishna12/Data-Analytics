import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
plt.step(df["Annual Salary"],df["Age"])
plt.show()