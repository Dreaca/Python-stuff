import pandas as pd
{
# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Age": [24, 30, 29, 27]
# }

# df = pd.DataFrame(data)

# #Locating cell by row index and column label
# # print(df.loc[1, "Name"])

# # #locating cell by row index and column index
# # print(df.iloc[1,0])

# # #Selecting cell 
# # print(df.loc[1])

# #Selecting multiple rows

# print(df.loc[[0,2]])


# data = {
#     "Calories" : [420,380,390]
#     ,"duration":[50,40,45]

# df = pd.DataFrame(data, index=["day1","day2","day3"]) #giving indexes labels 

# print(df)

# print(df.loc["day1"]) selecting rows from labels

# print(df.loc["day2":"day3"]) # selecting multiple rows

# print(df["Calories"])

# print(df.shape)

# print(df.columns)

# print(list(df.columns))

# print(df.size)

# print(df.values) returns values as a numpy array

# print(len(df)) returns the number of rows

# print(df.mean()) returns the mean of all columns

# print(df.sum()) returns the sum of all values in each column

# print(df.describe()) returns the statistic for each column

#Filtering rows in a DataFrame

# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Age": [24, 30, 29, 27]
# }

# df = pd.DataFrame(data)

# filtered = df[df["Age"]>25]

# print(filtered, type(filtered))

#Adding a new row 

# df.loc[len(df)] = ["John", 25]

# print(df, type(df))

#Deleting a Column

# print (df.drop('Age', axis=1))

#Deleting a row

# print(df.drop(3, axis=0))
}
df = pd.read_csv("Day07/customers-100.csv")

print(df)

djson = pd.read_json("Day07/student.json")

print(djson)