#creation of data frame
import pandas as pd
data = {" name " : ["john","krishna","janvi"],
        "Age": [23,18,40],
        "Salary": [20000,30000,40000]}
df = pd.DataFrame(data)
print(df)

#import from excel file
data = pd.read_csv("C:Users/krish/OneDrive/hotel_bookings_upadted.csv")
print(data)

#from the folder
data1 = pd.read_excel("hotel_bookings_upadted.xlsx")
print(data1)