import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {"Days":[1,2,3,4,5],
        "NOP":[10,23,36,47,50]}
df = pd.DataFrame(data)
print(df)
sns.lineplot(data=data,x="Days",y="NOP")
plt.show()
