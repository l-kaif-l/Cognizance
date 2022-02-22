number = int(input("Enter a number"))
temprory = number
summ = 0
remainder = 0
while number > 0:
    remainder = number % 10
    summ = (summ*10) + remainder
    number = number//10
if temprory == summ:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
    
