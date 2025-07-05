import pandas as pd
import matplotlib.pyplot as pl

data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
df2 = df.head(50)
x = df2["Age"]
y1 = df2["Annual Salary"]

pl.stackplot(x, y1)

pl.show()