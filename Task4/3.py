# Importing pandas library into the program with the object name or reference as pd
import pandas as pd
# Creating a List
d = [["Abc", 12, 95],
     ["Def", 11, 88],
     ["Ghi", 14, 90]]
df= pd.DataFrame(d, index=[1, 2, 3], columns=["Name", "Roll Number", "Marks"])
print(df)
#Printing the second row/ record from the table created
print(df[1:2])