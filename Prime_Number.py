# Prime number program in Python
num = int(input("Enter a number: "))
cnt = 0 
''' 
In Python, there are no increment (++) or decrement (--) operators 
like in C, C++, or Java. Instead, you use += and -= operators to 
increase or decrease a value.
'''
# range will start from 2 to < n
for i in range(2, num):
    if num % i == 0:
        cnt+=1
        break
if cnt == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

