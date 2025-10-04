n = int(input("Enter the Number : = "))
fact = 1 
for i in range(1,n+1): # starts from 1 and till less than n+1 means 6 
    fact *= i
print("The Factorial of Number is : = ",fact)