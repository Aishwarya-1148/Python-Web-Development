# the fibo series 

print("THe Fibo series id as above : = \n")

n1 , n2 = 0 , 1 
n = int(input("Enter the hpw many fibo digits u want : = ")) # 10 

for i in range(n+1):
    print(n1 , end =" , ")
    n1 , n2 = n2 , n1+n2
    
# 0 , 1 , 1 , 2 , 3 , 5 , 