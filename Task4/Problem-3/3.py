
import pandas as pd
table = []

count = int(input("Enter number of students: "))

for i in range(0, count):
    print("Enter details of each student in R.No., Name, Marks format: \n")
    table.append([])
    for j in range(0, 3):
        Enter_details = input()
        table[i].append(Enter_details)

print(table)
df = pd.DataFrame(table, columns=["R.No.", "Name", "Marks"])
print(df)
print(df[1:2])

