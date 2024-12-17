import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 29, 27]
}

df = pd.DataFrame(data)

#Locating cell by row index and column label
# print(df.loc[1, "Name"])

# #locating cell by row index and column index
# print(df.iloc[1,0])

# #Selecting cell 
# print(df.loc[1])

#Selecting multiple rows

print(df.loc[[0,2]])