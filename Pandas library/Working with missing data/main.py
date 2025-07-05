import pandas as pd
import numpy as np
data = pd.read_csv("C:Users/krish/OneDrive/hotel_bookings_upadted.csv")
print(data)
print(data.isnull().sum())
print(data.dropna().isnull().sum()) #it will drop the null values
data["country"] = data ["country"].replace(np.nan,"india") #the null value in country row is change to india
print(data)
print(data["adults"].mean())