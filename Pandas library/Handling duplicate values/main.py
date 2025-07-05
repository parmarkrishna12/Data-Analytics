import pandas as pd
data = pd.read_csv("C:Users/krish/OneDrive/hotel_bookings_upadted.csv")
print(data)
#find duplicated
print(data.duplicated())#shows in boolean values
print(data["hotel"].duplicated().sum())
print(data.drop_duplicates("hotel"))#delets the duplicates

