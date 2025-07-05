import pandas as pd

data = pd.read_csv("c:Users/krish/OneDrive/hotel_bookings.csv")
print(data)
print(data.head(10)) # starting 10
print(data.tail(10)) #last 10
print(data.info()) #shows the data type and also memory usage
print(data.describe()) #shows the percentage of the data
print(data.isnull().sum())# shows column wise null value


