string = input("Enter a string: ")
print(string)
l = len(string)
for i in range(0,l):
    if i%2 == 0:
        print(string[i])
    
