n = int(input("Enter the number to Reverse : = "))

reversed = 0 
og = n 
while n != 0:
    remainder = n % 10 
    reversed = reversed + (remainder * remainder * remainder )
    n //= 10 # we should use // not /

if og == reversed :
    print(f"The Number {og} Is Armstrong Number ")
else :
    print(f"The NUmber {og} is Not a Armstrong Number")

