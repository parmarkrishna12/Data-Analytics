import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
sns.pairplot(data,hue="day")
plt.show()