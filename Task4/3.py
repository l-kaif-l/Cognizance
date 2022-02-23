
import pandas as pd
table = []

count = int(input("Enter number of students: "))

for i in range(0,3):
    print("Enter details of each student in R.No., Name, Marks format: \n")
    table.append([])
    for j in range(0, count):
        Enter_details = input()
        table[i].append(Enter_details)

print(table)
df = pd.DataFrame(table, index=[1, 2, 3], columns=["R.No.", "Name", "Marks"])
print(df)
print(df[1:2])

