# Getting a String from user using input() function
string = input("Enter a string: ")
print(string)
# Retrieving the length of the Entered String
l = len(string)

for i in range(0,l):
    if i%2 == 0:    # We know that a even number mod 2 gives us 0, so by using this condition we are retrieving the even numbers and
        # and using them we are printing the even index characters from the string
        print(string[i])
    
