
import pandas as pd
d = [["Abc", 12, 95],
      ["Def", 11, 88],
      ["Ghi", 14, 90]]
df= pd.DataFrame(d, index=[1, 2, 3], columns=["Name", "Roll Number", "Marks"])
print(df)
print(df[1:2])
